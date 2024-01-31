from django import forms

# Form css style class
login_form = 'form-control'


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50, 
        widget=forms.TextInput(
            attrs={
                'class': login_form, 
                'id': 'floatingInput', 
                'name': "username", 
                'placeholder': "Username"
            }
        ), 
        required=True
    )
    password = forms.CharField(
        max_length=30, 
        widget=forms.PasswordInput(
            attrs={
                'class': login_form, 
                'id':'floatingPassword', 
                'name': "password", 
                'placeholder': "Password"
            }
        ), 
        required=True
    )