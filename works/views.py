import json

from django import http
from django.shortcuts import render
from django.views.generic import FormView

from accounts import serializers
from works import serializers
from utils.response import ServerErrorJsonResponse, BadRequestJsonResponse
from works.forms import WorksForm


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
