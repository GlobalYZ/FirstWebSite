from django.urls import path

from works import views

urlpatterns = [
    # 作品上传
    path('api/artwork/', views.ArtWork.as_view(), name='works_api_artwork'),
    # 作品列表信息
    path('api/list/', views.WorkListView.as_view(), name='works_api_list'),
    # 作品详细信息
    path('api/detail/<int:pk>/', views.ArtWorkDetailView.as_view(), name='works_api_detail'),
    # 作品的评论列表
    path('api/comment/list/<int:pk>/', views.CommentListView.as_view(), name="works_comment_list"),

]