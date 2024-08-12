from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description', 'parent', 'wake_up_time', 'day_of_week', 'date', 'location']
        widgets = {
            'wake_up_time': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }