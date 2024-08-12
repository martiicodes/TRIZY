import json
from django.http import HttpResponse
from django.views.generic import ListView
from django.utils import timezone
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import TodoItem

class TodoListView(ListView):
    model = TodoItem
    template_name = 'todo_app/todo_list.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now()
        context['wake_up_time'] = self.request.session.get('wake_up_time', '')
        context['location'] = self.request.session.get('location', '')
        return context

    def get_queryset(self):
        return TodoItem.objects.filter(parent=None)

@require_POST
def update_info(request):
    request.session['wake_up_time'] = request.POST.get('wake_up_time')
    request.session['location'] = request.POST.get('location')
    messages.success(request, 'Information updated successfully.')
    return redirect('todo_list')

def export_todos(request):
    todos = TodoItem.objects.all()
    data = {
        'date': timezone.now().strftime('%Y-%m-%d'),
        'wake_up_time': request.session.get('wake_up_time', ''),
        'location': request.session.get('location', ''),
        'todos': [{'title': todo.title, 'description': todo.description, 'parent': todo.parent_id} for todo in todos]
    }
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response['Content-Disposition'] = f'attachment; filename=todos_{timezone.now().strftime("%Y%m%d")}.json'
    return response