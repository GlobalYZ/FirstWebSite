from django.urls import path
from system import views

urlpatterns = [
    path('slider/list/', views.slider_list, name="slider_list"),
    path('question/list/', views.question_list, name="question_list"),
    # 发送验证码
    path('send/sms/', views.SmsCodeView.as_view(), name="send_sms"),
]