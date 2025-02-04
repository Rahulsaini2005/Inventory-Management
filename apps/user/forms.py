from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.urls import reverse
from rest_framework import serializers

User = get_user_model()




class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_active', 'password1', 'password2']


class EditUserForm(UserChangeForm):
    email = forms.EmailField(required=True)
    password_help_text ="Raw passwords are not stored, so there is no way to see this \n customer's password, but you can change the password using \n <a href=\"{}\">this form</a>."

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_active', 'password']

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        password = self.fields.get('password')
        # if password:
        #     password.help_text = self.password_help_text.format(reverse('customer-change-password', kwargs={'user_id': self.instance.id}))


class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserSignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EditUserProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']