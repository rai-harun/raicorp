from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from todo.models import Todo

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Todo.objects.create(user=instance)
        print('A todo created!')

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.todo.save()
        print('A todo updated!')