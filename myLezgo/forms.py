from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Order


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ('name', 'surname', 'number', 'city', 'car', 'fullFuel', 'water', 'driver', 'outOfTown', 'sweets', 'comments')

        # widgets ={
        #     'name': TextInput(attrs={
        #         'placeholder': 'Your name'
        #     }),
        #     'surname': TextInput(attrs={
        #         'placeholder': 'Your surname'
        #     }),
        #     'number': TextInput(attrs={
        #         'placeholder': '+7 (000) 000-00-00'
        #     }),
        #     'city': Select(attrs={
        #
        #     }),
        #     'car': RadioSelect(attrs={
        #         'class': 'for-checkbox-tools buttontake'
        #         'id':
        #     }),
        #     'fullFuel': CheckboxInput(attrs={
        #
        #     }),
        #     'water': TextInput(attrs={
        #
        #     }),
        #     'driver': TextInput(attrs={
        #
        #     }),
        #     'outOfTown': TextInput(attrs={
        #
        #     }),
        #     'sweets': TextInput(attrs={
        #
        #     }),
        #     'comments': TextInput(attrs={
        #
        #     }),
        # }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserCreationForm, self).__init__(*args, **kwargs)

        username_widget = forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
        username_field = forms.CharField(label="Username", widget=username_widget)
        self.fields["username"] = username_field

        login_widget = forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
        login_field = forms.EmailField(label="Email", widget=login_widget)
        self.fields["email"] = login_field

        pass1_widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
        pass1_field = forms.CharField(label="Password", widget=pass1_widget)
        self.fields["password1"] = pass1_field

        pass2_widget = forms.PasswordInput(attrs={'placeholder': 'Re-Password', 'class': 'form-control'})
        pass2_field = forms.CharField(label="Password(again)", widget=pass2_widget)
        self.fields["password2"] = pass2_field
