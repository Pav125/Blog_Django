from django.db.models.signals import post_save # this a signal that gets fired  that Django sends when an object is saved
from django.contrib.auth.models import User
from django.dispatch import receiver # this is to define receiver fun and perform a task
from .models import Profile

@receiver(post_save, sender=User)  # when user object is saved in the database then call this function
def create_profile(sender, instance, created, **kwargs): #  here we are creating a new profile every time a user is created
    if created: #  check whether it's new or existing one
        Profile.objects.create(user=instance) #  creating profile for every new user
        
# **kwargs means the fun will accept any other keyword arguments

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
    
    