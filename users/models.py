from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#model with one to one relatiomship

class Profile(models.Model): # this is the parent class/table for our user profile
    """A model representing a user profile."""
    user = models.OneToOneField(User, on_delete = models.CASCADE) # this creates the One To One relationship between the User and Profile Models 
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics') # this will store the path of the uploaded file in the project folder named "profile_pics"
    
    # dunder str  method, which returns string representation of object
    def __str__(self):
        return f'{self.user.username} Profile'  # returns username and profile when called in string format