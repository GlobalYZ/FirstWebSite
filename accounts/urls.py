from django.urls import path

from accounts import views

urlpatterns = [
    # 登录和退出的接口
    path('user/api/login/', views.user_api_login, name='user_api_login'),
    path('user/api/logout/', views.user_api_logout, name='user_api_logout'),
    # 用户详细信息接口
    path('user/api/info/', views.UserDetailView.as_view(), name='user_api_info'),
    # 用户注册
    path('user/api/register/', views.UserRegisterView.as_view(), name='user_api_register'),
    # 用户修改
    path('user/api/modify/', views.UserModifyView.as_view(), name='user_api_register'),
    # 头像上传
    path('user/api/avatar/', views.UserAvatar.as_view(), name='user_api_avatar'),
    # 头像上传
    # path('user/test/avatar/', views.User_Avatar.as_view(), name='user_test_avatar'),
]