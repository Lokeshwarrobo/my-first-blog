from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('articles/',views.ArticleListView.as_view(),name='Articles'),
    path('article/<int:pk>',views.ArticleDetailView.as_view(),name= 'article_page'),
    path('article/new/',views.ArticleCreateView.as_view(),name='new_article'),
    path('article/<int:pk>/edit',views.ArticleUpdateView.as_view(),name='article_edit'),
    path('article/<int:pk>/delete',views.ArticleDeleteView.as_view(),name='article_delete'),
    path('signup/',views.SignupView.as_view(),name='signup'),


]