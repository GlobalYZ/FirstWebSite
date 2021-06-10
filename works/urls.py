from django.urls import path

from works import views

urlpatterns = [
    # 作品上传
    path('api/artwork/', views.ArtWork.as_view(), name='works_api_artwork'),
    # 作品列表信息
    path('api/list/', views.WorkListView.as_view(), name='works_api_list'),

]