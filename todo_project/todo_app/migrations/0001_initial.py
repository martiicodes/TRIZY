# Generated by Django 4.2.15 on 2024-08-12 10:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('wake_up_time', models.TimeField(blank=True, null=True)),
                ('day_of_week', models.CharField(blank=True, max_length=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='todo_app.todoitem')),
            ],
        ),
    ]
