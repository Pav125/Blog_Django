from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post) #this will create a new post in the admin page with all of its fields visible to be edited by admins only