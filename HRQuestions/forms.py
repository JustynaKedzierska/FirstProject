from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User

from .models import QuestionList


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        field_classes = {'username': UsernameField}


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)


class ResetPasswordForm(forms.Form):
    password = forms.CharField(label="Podaj nowe hasło", widget=forms.PasswordInput, max_length=10)
    confirm_password = forms.CharField(label="Potwierdź hasło", widget=forms.PasswordInput, max_length=10)

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Hasła się różnią",
            )
        return password2


class QuestionListModelForm(forms.ModelForm):
    class Meta:
        model = QuestionList
        fields = ['name', 'author', 'questions']
        widgets = {
            'questions': forms.CheckboxSelectMultiple()
        }


class QuestionUpdateModelForm(forms.ModelForm):
    class Meta:
        model = QuestionList
        fields = ['name', 'author', 'questions']
        widgets = {
            'questions': forms.CheckboxSelectMultiple()
        }