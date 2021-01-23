from django.db.models.signals import post_save  # This is so that we can add images automatically
from django.contrib.auth.models import User # This is the sender that sends the message
from django.dispatch import receiver # This is what actually does something with the signal
from .models import Profile

@receiver(post_save,sender=User) # WHen a user is saved send this siganl which will send that signal back into the function and then run everything
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=User) # WHen a user is saved send this siganl which will send that signal back into the function and then run everything
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
