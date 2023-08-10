# from django import forms
# from signup.models import Sign_Up
    
# class SignUp_Form(forms.ModelForm):
#     class Meta:
#         model = Sign_Up
#         fields = "__all__"
        
#         labels = {'name':'Name', 'pwd':'Password', 'contact_num':'Contact Number', 'address':'Address', 'img':'Image'}    
  
#         widgets = {
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             'pwd':forms.PasswordInput(attrs={'class':'form-control'}),
#             'contact_num':forms.NumberInput(attrs={'class':'form-control'}),
#             'address':forms.TextInput(attrs={'class':'form-control'}),
#             'img':forms.FileInput()
#         }

# *************************************************************************

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Sign_up(UserCreationForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
    
   