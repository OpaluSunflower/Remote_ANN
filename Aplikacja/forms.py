from django import forms

class UserForm(forms.Form):
    email = forms.EmailField(max_length = 100,label='email')
    username=forms.CharField(max_length=100,label='username')

class LoginForm(forms.Form):
    loginClass=forms.TextInput(attrs={'class':'form-control'})
    passwordClass=forms.PasswordInput(attrs={'class':'form-control'})
    login = forms.CharField(widget=loginClass,label='login',max_length=100, required=True)
    password = forms.CharField(widget=passwordClass,label='email',max_length=100, required=True)

class RegisterForm(forms.Form):
    txtClass=forms.TextInput(attrs={'class':'form-control'})
    passwordClass=forms.PasswordInput(attrs={'class':'form-control'})
    login = forms.CharField(widget=txtClass,label='login',max_length=100, required=True)
    email = forms.CharField(widget=txtClass,label='email',max_length=100, required=True)
    password = forms.CharField(widget=passwordClass,label='password',max_length=100, required=True)