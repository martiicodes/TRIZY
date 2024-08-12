from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('update-info/', views.update_info, name='update_info'),
    path('export/', views.export_todos, name='export_todos'),
]
