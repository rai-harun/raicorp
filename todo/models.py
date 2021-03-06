from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.forms.utils import to_current_timezone

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo", null=True)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

