from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Metadata, in a general sense, refers to data that provides information about other data. It describes various aspects of data, helping users, systems, or processes understand and manage the data effectively

class UserRegisterForm(UserCreationForm): #  new form class inheriting properties of UserCreationForm
    email = forms.EmailField() #  add an EmailField to the form, which is a field for emails 
    # email = forms.EmailField(required='True')(required='True' by default )  takes care of validating that it's actually an email address
    class Meta: # to provide metadata about the model,it gives nested namespace for configurations and keeps the configurations in place
        model = User # when we  create a new user (perform form.save() ), it will be based(saved) on this model (user)
        fields = [ 'username', 'email', 'password1', 'password2' ] # this line is for  which fields to include, not necessary if we use all of them
        

class UserUpdateForm(forms.Modelform):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [ 'username', 'email']
        
    