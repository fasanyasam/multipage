from django import forms 
class FormName(forms.Form):
    email= forms.EmailField()
    password= forms.PasswordInput()