from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm #used to import  the user creation form for  new users
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST) #creates a form based on the data submitted in the request
        if form.is_valid(): #checks whether or not the form is valid
            form.save()  #saves the new user to the database
            username = form.cleaned_data.get('username') #this  line of code gets the username field out of the cleaned data (it will convert all into py types)which is a dictionary containing all the data
            messages.success(request,f'Your account has been created! You are now able to login')  #displays message when account is successfully made
            return redirect('login') #redirects the user to the home page once they have registered successfully
            
    else:
        form = UserRegisterForm() #if it's not a POST request, create an empty form
    return render(request, 'users/register.html', {'form': form})   #used for  rendering the html page with the registration form 
    #create an instance of the user creation form
    # {'form' : form} is a dictionary that will be passed into the template, and it contains our form object

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
#flas hmessage are  used to send messages to the user after performing certain actions like registration
# that only displayed once disappears when  the message has been read by the user and reloades the page

def logout_view(request):
    logout(request) # this function logs out the current logged-in user
    return render(request, 'users/logout.html') # this  redirects the user to a specific url (the login page)
    
@login_required #this decorator restricts access to users who ar already logged in
def profile(request):
    return render(request, 'users/profile.html')

#decorators are  functions that modify the behavior of other functions. In this case we use @login_required to make sure that you can only see this view