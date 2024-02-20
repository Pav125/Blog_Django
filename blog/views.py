from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

#dummy data
# posts=[
#     {
#         'author':  'John Doe',
#         'title': 'Blog Post 1',
#         'content': 'First Post  Content...',
#         'date_posted': 'August 23,2024'
#     },
#     {
#         'author':  'Pavan',
#         'title': 'Blog Post 2',
#         'content': 'Second Post  Content...',
#         'date_posted': 'August 24,2024'
#     }
# ]

def home(request):
    context={
        'posts': Post.objects.all()  #'posts' is key
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})