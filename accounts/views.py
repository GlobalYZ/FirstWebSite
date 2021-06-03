import json

from django import http
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.base import View

from accounts.forms import LoginForm, RegisterForm, ModifyForm
from utils.response import BadRequestJsonResponse, MethodNotAllowedJsonResponse, UnauthorizedJsonResponse, \
    ServerErrorJsonResponse
from accounts import serializers

def user_api_login(request):
    """ 用户登录接口-POST """
    # 获取输入的内容
    if request.method == 'POST':
        # 表单验证
        form = LoginForm(request.POST)
        # 如果通过了验证，执行登录
        if form.is_valid():
            user = form.do_login(request)
            # 返回内容：用户的信息（用户的基本信息、详细信息）
            profile = user.profile# 1对1的反向查询，返回一个profile对象
            data = {
                'user': serializers.UserSerializer(user).to_dict(),
                'profile': serializers.UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data)
            # return HttpResponse("oK")
        else:
            # 如果没有通过表单验证，返回表单的错误信息
            err = json.loads(form.errors.as_json())# form.errors.as_json()就是一个json，通过.loads转换成python对象
            return BadRequestJsonResponse(err)# 因为这个函数里要放入python对象,err里装的就是form里raise抛出的错误信息
    else:
        # 请求不被允许
        return MethodNotAllowedJsonResponse()


def user_api_logout(request):
    """ 用户退出接口 """
    logout(request)# from django.contrib.auth import logout
    return http.HttpResponse(status=201)# 给一个201的状态码说明已经退出了


class UserDetailView(View):
    """ 用户详细接口 ，这个地方不适用于@login_required，因为是前后端分离"""
    def get(self, request):# 登录完成之后，Django会把user设置到request这个模块里去
        # 获取用户信息
        user = request.user
        # 用户：是游客吗？
        if not user.is_authenticated:
            # 返回401状态码
            return UnauthorizedJsonResponse()
        else:
            # 返回详细信息
            profile = user.profile
            data = {
                'user': serializers.UserSerializer(user).to_dict(),
                'profile': serializers.UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data)


def user_api_register(request):
    """ 用户注册 """
    # 1. 表单，验证用户输入的信息（用户名、昵称、验证码）
    # 2. 创建用户基础信息表、用户详细信息表
    # 3. 执行登录
    # 4. 保存登录日志
    pass


class UserRegisterView(FormView):# 继承FormView，里面有form_valid和form_invalid方法，重写即可
    """ 用户注册接口 """
    form_class = RegisterForm
    http_method_names = ['post']# 只能是post请求，其他方式不被允许

    def form_valid(self, form):
        """ 表单已经通过验证 """
        result = form.do_register(request=self.request)
        if result is not None:
            user, profile = result
            data = {
                'user': serializers.UserSerializer(user).to_dict(),
                'profile': serializers.UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data, status=201)
        return ServerErrorJsonResponse()

    def form_invalid(self, form):
        """ 表单没有通过验证 """
        err_list = json.loads(form.errors.as_json())
        return BadRequestJsonResponse(err_list)



class UserModifyView(FormView):
    """ 用户修改信息 """
    form_class = ModifyForm
    http_method_names = ['post']

    def form_valid(self, form):
        """ 表单已经通过验证 """
        result = form.modify(request=self.request)
        if result is not None:
            user, profile = result
            data = {
                'user': serializers.UserSerializer(user).to_dict(),
                'profile': serializers.UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data, status=201)
        return ServerErrorJsonResponse()

    def form_invalid(self, form):
        """ 表单没有通过验证 """
        err_list = json.loads(form.errors.as_json())
        return BadRequestJsonResponse(err_list)