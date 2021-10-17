from django.contrib import admin
from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    #path('home/',views.post_home),
    path('<int:id>/', views.post_detail,name='detail'),
    path('create/', views.post_create,name='create'),
    path('<int:id>/update/', views.post_update,name='update'),
    path('<int:id>/delete/', views.post_delete,name='delete'),
    path('',views.post_list, name='list')
    ]
