from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('update/<str:pk>/', views.update, name='update'),
]