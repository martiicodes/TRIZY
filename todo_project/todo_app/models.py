from django.db import models
from django.utils import timezone

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    wake_up_time = models.TimeField(null=True, blank=True)
    day_of_week = models.CharField(max_length=10, blank=True)
    date = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title