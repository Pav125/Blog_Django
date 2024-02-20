from django.db import models
from django.utils import timezone # Used to  get the current time so we can add it to our blog posts.
from django.contrib.auth.models import User #  Import the user model for authentication
from django.urls import reverse # Used to generate URLs by reversing URL patterns

# Create your models here
# this code will connect db  with our app, and create a table called 'Post' in the database
# Post is a class that inherits properties/methods from Django's base Model class
# each field inside the class represents a column in the database table
# CharField - string (up to 256 characters)
# ForeignKey -  a reference to another model (User)
# DateTimeField - a date and time

#Post is a model  for individual blog posts
class Post(models.Model): # models.Model is the base class for all models in Django
    title = models.CharField(max_length = 100)
    content = models.TextField() #unrestricted text like lines lines of data
    #date_posted = models.DateTimeField(auto_now = True) #auto_now = True  means that the field will be set to now every time a save is made, auto_now_
    #date_posted = models.DateTimeField(auto_now_add=True) #auto_now_add=True  means that the field will be set to now when the object is created, and auto_now=
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #.PROTECT, .RESTRICT
    #author: A foreign key field referencing the built-in User model, indicating that 
    # each post is associated with a specific user. The on_delete=models.CASCADE
    # argument means that if a user is deleted, all associated posts will be deleted as well.
    
    # ForeignKey is used to create a many-to-one relationship between the Post model and the-in `User model provided by Django's authentication system.

    # A ForeignKey in Django is a field that establishes a relationship two models, where one model can be associated with multiple of another model. In this case, each Post instance is associated with a single User instance, while each User instance can have multiple Post instances associated with them.

    def __str__(self):    
        return self.title 
    # __str__ method, a built-in Python method for creating a string representation of the object. In this case, it returns the title of the post, making it easier to read and understand when printed.
    

    # def get_absolute_url(self):
    #     return reverse('blog-detail',args=[str(self.id)])