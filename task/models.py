from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title