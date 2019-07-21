from django import forms
# from django.contrib.auth.models import User

# class UserLoginForm(forms.Form):
#     userName=forms.CharField()
#     userPassword=forms.CharField()
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class UserRegisterForm(forms.ModelForm):
    password=forms.CharField()
    password2=forms.CharField()

    class Meta:
        model=User
        fields=('username','email')


    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):

            return data.get('password')
        else:
            print("密码输入不一致,请重试")
            raise forms.ValidationError("密码输入不一致,请重试。")


