from django import forms
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox



class RegisterForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password':forms.PasswordInput(),
        }