from django.urls import path

from . import views

app_name = 'myFirstApp'
urlpatterns = [
    # localhost:8000
    path('', views.index, name='index'),

    # localhost:8000/article/id
    path('article/<int:article_id>/', views.article, name='article'),

    # localhost:8000/search/id
    path('search/<str:article_text>/', views.search, name='search'),

    # localhost:8000/archive
    path('archive/', views.archive, name = 'archive'),

    # localhost:8000/article/id/comments_block
    path('article/<int:article_id>/comments_block', views.showComments, name='comments_block')

]
