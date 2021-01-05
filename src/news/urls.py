from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.category, name='category'),
    path('category/', views.category, name='category')
]