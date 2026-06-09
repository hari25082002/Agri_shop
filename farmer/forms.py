from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Farmer  

class Registration_form(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2','required':'required'})
    )
    name = forms.CharField(
        max_length=150, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2','required':'required'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-2','required':'required'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control mt-2','required':'required'})
    )                      
    phone_number = forms.CharField(
        max_length=20, 
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control mt-2','required':'required'})
    )
    address = forms.CharField(
        max_length=200, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2','required':'required'})
    )
    city = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2','required':'required'})                        
    )
    profile_pic = forms.ImageField(
        required=True, 
        widget=forms.ClearableFileInput(attrs={'class': 'form-control mt-2'})
    )
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Farmer.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already associated with another account.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if Farmer.objects.filter(phonenumber=phone_number).exists():
            raise ValidationError("This phone number is already registered.")
        return phone_number

class Farmer_info_update(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2','required':'required'})
    )
    name = forms.CharField(
        max_length=150, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2','required':'required'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control mt-2','required':'required'})
    )                      
    phone_number = forms.CharField(
        max_length=20, 
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control mt-2','required':'required'})
    )
    address = forms.CharField(
        max_length=200, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2','required':'required'})
    )
    city = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2','required':'required'})                        
    )
    profile_pic = forms.ImageField(
        required=True, 
        widget=forms.ClearableFileInput(attrs={'class': 'form-control mt-2'})
    )

class CreateProductForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'required': 'required'})
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control mt-2', 'required': 'required'})
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control mt-2', 'required': 'required'})
    )
    quantity = forms.IntegerField(  
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control mt-2', 'required': 'required'})
    )
    shipping_area = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control mt-2', 'required': 'required'})
    )
    product_image = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control mt-2'})
    )

class Product_Update(forms.Form):
    name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'required': 'required'})
    )

    description = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'required': 'required'})
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control mt-2', 'required': 'required'})
    )
    quantity = forms.IntegerField(  
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control mt-2', 'required': 'required'})
    )
    shipping_area = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'required': 'required'})
    )
    product_image = forms.ImageField(
        required=False, 
        widget=forms.ClearableFileInput(attrs={'class': 'form-control mt-2'})
    )

class ProductDeleteConfirmationForm(forms.Form):
    product_name = forms.CharField(max_length=255, label='Product Name')
    password = forms.CharField(widget=forms.PasswordInput(), label='Your Password')