"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views #importing views directly (without creating url.py in user directry) so we can use them in our urls without having to reference the whole module every time
from django.conf import settings # imported to allow access to settings in our urls file
from django.conf.urls.static import static # for serving media files in development mode (DEBUG = True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('profile/', user_views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name= 'login'),
    # path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('logout/', user_views.logout_view, name="logout"), # Custom logout view
    # path('blog/', include('blog.urls'))
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# this code is  added so that Django serves media files in development mode 