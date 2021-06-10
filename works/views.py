import json

from django import http
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import FormView, ListView

from accounts import serializers
from works import serializers
from utils.response import ServerErrorJsonResponse, BadRequestJsonResponse, NotFoundJsonResponse
from works.forms import WorksForm
from works.models import Artwork


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
    paginate_by = 8
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
