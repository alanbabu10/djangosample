from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('delete/<int:id>/', views.delete_task),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
]