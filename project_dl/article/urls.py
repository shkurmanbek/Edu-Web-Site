from django.urls import path, include
import article.views
urlpatterns = [
    path('1/', article.views.basic_one),
    path('2/', article.views.template_two),
    path('3/', article.views.template_three_simple),
    path('articles/all/', article.views.articles),
    path('articles/get/<int:article_id>/', article.views.article),
    path('articles/addlike/<int:article_id>/', article.views.addlike),
    path('articles/addcomment/<int:article_id>/', article.views.addcomment),
    path('', article.views.articles),
]