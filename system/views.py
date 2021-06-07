import json

from django import http
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.db import connection

from system.forms import SendSmsCodeForm
from system.models import Slider, Questions
from utils.response import ServerErrorJsonResponse, BadRequestJsonResponse


def slider_list(request):
    """ 轮播图接口 """
    data = {
        'meta': {
        },
        'objects': []
    }
    queryset = Slider.objects.filter(is_valid=True)
    # 根据类型查询
    # types = request.GET.get('types', None)
    # if types:
    #     queryset = queryset.filter(types=types)
    for item in queryset:
        data['objects'].append({
            'types': item.types,
            'number': item.number,
            'img_url': item.img.url,# models模型定义的ImageField属性有url属性
            'target_url': item.target_url,
            'name': item.name
        })
    return http.JsonResponse(data)

def question_list(request):
    """ 常见问题接口 """
    data = {
        'meta': {
        },
        'objects': []
    }
    queryset = Questions.objects.filter(is_valid=True)
    # 根据类型查询
    types = request.GET.get('types', None)
    if types:
        queryset = queryset.filter(types=types)
    for item in queryset:
        data['objects'].append({
            'number': item.number,
            'title': item.title,
            'desc': item.desc
        })
    return http.JsonResponse(data)

# 用面向对象的方式来实现，比登录接口要简单
class SmsCodeView(FormView):
    form_class = SendSmsCodeForm
    # http_method_names = ['post']# 只能是post请求，其他方式不被允许
    def form_valid(self, form):# 重写
        """ 表单已经通过验证 """
        data = form.send_sms_code()
        if data is not None:# 说明验证码发送成功并且存在Redis里了
            return http.JsonResponse(data, status=201)
        return ServerErrorJsonResponse()
    def form_invalid(self, form):# 重写
        """ 表单没有通过验证 """
        err_list = json.loads(form.errors.as_json())
        return BadRequestJsonResponse(err_list)
