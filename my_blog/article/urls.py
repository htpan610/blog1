from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('article_list/', views.article_list, name='article_list'),
    # 新增article_detail的URL
    path('article_detail/<int:id>/', views.article_detail, name='article_detail'),
    path('', views.article_list, name='main_page')
]
