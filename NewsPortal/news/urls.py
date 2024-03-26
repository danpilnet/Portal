from django.urls import path
from .views import PostList, PostDetail, PostSearch


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('news/search/', PostSearch.as_view(), name= 'news_search'),
]