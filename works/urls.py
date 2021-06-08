from django.urls import path

from works import views

urlpatterns = [
    # 头像上传
    path('works/api/artwork/', views.ArtWork.as_view(), name='works_api_artwork'),
]