import json

from django import http
from django.db.models import Q
from django.views.generic import FormView, ListView, DetailView

from accounts import serializers
from works import serializers
from utils.response import ServerErrorJsonResponse, BadRequestJsonResponse, NotFoundJsonResponse
from works.forms import WorksForm
from works.models import Artwork, Comment


class ArtWork(FormView):
    """ 用户上传作品 """
    form_class = WorksForm
    http_method_names = ['post']

    def form_valid(self, form):
        """ 表单已经通过验证 """
        result = form.upload(request=self.request)
        if result is not None:
            user, artwork = result
            data = {
                'user': serializers.UserSerializer(user).to_dict(),
                'artwork': serializers.WorksSerializer(artwork).to_dict()
            }
            return http.JsonResponse(data, status=201)
        return ServerErrorJsonResponse()

    def form_invalid(self, form):
        """ 表单没有通过验证 """
        err_list = json.loads(form.errors.as_json())
        return BadRequestJsonResponse(err_list)

class WorkListView(ListView):
    """ 作品列表接口 """
    paginate_by = 2
    def get_queryset(self):
        """ 重写查询方法 """
        query = Q(is_valid=True)
        searchname = self.request.GET.get('searchname', None)
        if searchname:
            query = query & Q(name__icotains=searchname)
        queryset = Artwork.objects.filter(query)
        return queryset

    def get_paginate_by(self, queryset):
        """ 从前端控制每一页的分页大小 """
        page_size = self.request.GET.get('limit', None)
        return page_size or self.paginate_by

    def render_to_response(self, context, **response_kwargs):
        # 从关系型数据库拿数据
        page_obj = context['page_obj']
        if page_obj is not None:
            data = serializers.WorkListSerializer(page_obj).to_dict()
            return http.JsonResponse(data, status=201)
        else:
            return NotFoundJsonResponse()

class ArtWorkDetailView(DetailView):
    """ 作品详细信息 """

    def get_queryset(self):# 配置一下数据的来源
        # return Sight.objects.filter(is_valid=True)
        return Artwork.objects.all()

    def render_to_response(self, context, **response_kwargs):# 重写此函数
        page_obj = context['object']# 注意取的是object不是page_obj了
        if page_obj is not None:
            if page_obj.is_valid == False:
                return NotFoundJsonResponse()
            data = serializers.WorksSerializer(page_obj).to_dict()
            return http.JsonResponse(data)
        return NotFoundJsonResponse()

class CommentListView(ListView):
    """ 作品下的评论列表 """
    paginate_by = 10

    def get_queryset(self):
        # 根据作品ID查询作品
        artwork_id = self.kwargs.get('pk', None)
        artwork = Artwork.objects.filter(pk=artwork_id, is_valid=True).first()
        if artwork:
            # return Comment.objects.filter(is_valid=True, sight=sight)
            return artwork.comments.filter(is_valid=True)
        return Comment.objects.none()

    def render_to_response(self, context, **response_kwargs):
        """ 重写响应的返回 """
        page_obj = context['page_obj']# 此时所有的信息都在context里，page_obj里有分页信息和数据信息
        if page_obj is not None:
            data = serializers.CommentListSerializer(page_obj).to_dict()
            return http.JsonResponse(data)
        return  NotFoundJsonResponse()
