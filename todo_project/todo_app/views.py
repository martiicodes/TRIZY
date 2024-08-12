from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TodoItem
from .forms import TodoItemForm


# Create your views here.
class TodoListView(ListView):
    model = TodoItem
    template_name = 'todo_app/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return TodoItem.objects.filter(parent=None)

class TodoDetailView(DetailView):
    model = TodoItem
    template_name = 'todo_app/todo_detail.html'

class TodoCreateView(CreateView):
    model = TodoItem
    form_class = TodoItemForm
    template_name = 'todo_app/todo_form.html'
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = TodoItem
    form_class = TodoItemForm
    template_name = 'todo_app/todo_form.html'
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = TodoItem
    success_url = reverse_lazy('todo_list')
    template_name = 'todo_app/todo_confirm_delete.html'