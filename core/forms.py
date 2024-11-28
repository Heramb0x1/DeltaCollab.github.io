# from django import forms
# from .models import User  # Import the User model from your models.py file

# # Create a form for the User model
# class UserForm(forms.ModelForm):
#     # Define the choices for the education level field
#     EDUCATION_LEVEL_CHOICES = [
#         ('Undergraduate', 'Undergraduate'),
#         ('Pursuing PostGraduate', 'Pursuing PostGraduate'),
#         ('Post Graduate', 'Post Graduate'),
#         ('Pursuing PhD', 'Pursuing PhD'),
#         ('PhD', 'PhD'),
#     ]

#     # Add the education_level field to the form
#     education_level = forms.ChoiceField(choices=EDUCATION_LEVEL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User  # Specify the model
#         fields = ['username', 'password', 'email', 'availability', 'profile_picture', 'credits']  # Include other fields from the User model
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    education_level = forms.CharField(max_length=100)
    
    # Add other fields as needed

