import json

from django import http
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.db import connection

from system.forms import SendSmsCodeForm
from system.models import Slider
from utils.response import ServerErrorJsonResponse, BadRequestJsonResponse


def slider_list(request):
    """ 轮播图接口
    {
        "meta": {},
        "objects": []
    }
    """
    data = {
        'meta': {

        },
        'objects': []
    }
    queryset = Slider.objects.filter(is_valid=True)
    # 根据类型查询
    types = request.GET.get('types', None)
    if types:
        queryset = queryset.filter(types=types)
    for item in queryset:
        data['objects'].append({
            'id': item.id,
            'img_url': item.img.url,# models模型定义的ImageField属性有url属性
            'target_url': item.target_url,
            'name': item.name
        })
    # return HttpResponse(data) 如果是用这个，返回得到的是一个"metaobjects"字符串
    return http.JsonResponse(data)


def cache_set(request):
    """ 写缓存 """
    cache.set('username', 'lisi')
    # 5之后自动删除
    cache.set('password', 'password', timeout=5)
    return HttpResponse('ok')


def cache_get(request):
    """ 读缓存 """
    value = cache.get('username')
    return HttpResponse(value)


def send_sms(request):
    pass
    # 1. 拿到手机号，判断是否为真实的手机号码

    # 2. 生成验证码，并存储
    # TODO 3. 调用短信的发送接口
    # 4. 告诉用户验证码发送是否成功（会把验证码直接告诉用户）

# 用面向对象的方式来实现，比登录接口要简单
class SmsCodeView(FormView):
    form_class = SendSmsCodeForm
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
