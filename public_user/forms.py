from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Public_user
import datetime


class Public_registration_form(forms.Form):
    username=forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mt-2','required':'required'})
    )
    name=forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mt-2','requried':'requried'})
    )
    password=forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control mt-2','requried':'requried'})
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
    pincode = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control mt-2','required':'required'})                        
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
        if Public_user.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already associated with another account.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if Public_user.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("This phone number is already registered.")
        return phone_number
    
class Public_info_updateform(forms.Form):
    username=forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mt-2','required':'required'})
    )
    name=forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mt-2','requried':'requried'})
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
    pincode = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control mt-2','required':'required'})                        
    )
    profile_pic = forms.ImageField(
        required=True, 
        widget=forms.ClearableFileInput(attrs={'class': 'form-control mt-2'})
    )

class Order_form(forms.Form):
    name=forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mt-2','requried':'requried'})
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
    pincode = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control mt-2','required':'required'})                        
    )


class PaymentForm(forms.Form):
    PAYMENT_METHODS = [
        ('Card', 'Credit/Debit Card'),     
        ('Cash', 'Cash on Delivery'),       
        ('Netbanking', 'Bank Transfer'),     
        ('UPI', 'UPI'),                     
    ]

    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHODS,
        required=True,
        initial='Card',                     
        label="Payment Method"
    )


    card_number = forms.CharField(required=False, label='Card Number')
    expiration_date = forms.CharField(required=False, label='Expiration Date (MM/YY)')
    cvv = forms.CharField(required=False, label='CVV')
    
    bank_account = forms.CharField(required=False, label='Bank Account Number')
    bank_name = forms.CharField(required=False, label='Bank Name')

    upi_id = forms.CharField(required=False, label='UPI ID')

    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get("payment_method")

        if payment_method == 'Card':
            card_number = cleaned_data.get("card_number")
            expiration_date = cleaned_data.get("expiration_date")
            cvv = cleaned_data.get("cvv")

            if not card_number:
                self.add_error('card_number', "Card number is required.")
            elif len(card_number.replace(" ", "")) != 16:  
                self.add_error('card_number', "Invalid card number format. It must be 16 digits.")
            if not expiration_date:
                self.add_error('expiration_date', "Expiration date is required.")
            else:
                try:
                    month, year = map(int, expiration_date.split('/'))
                    if month < 1 or month > 12:
                        self.add_error('expiration_date', "Invalid month. Please enter a month between 01 and 12.")
                    current_year = datetime.date.today().year % 100
                    if year < current_year: 
                        self.add_error('expiration_date', "Card has expired.")
                except ValueError:
                    self.add_error('expiration_date', "Expiration date must be in the format MM/YY.")
            if not cvv:
                self.add_error('cvv', "CVV is required.")

        elif payment_method == 'Netbanking':
            bank_account = cleaned_data.get("bank_account")
            bank_name = cleaned_data.get("bank_name")

            if not bank_account:
                self.add_error('bank_account', "Bank account number is required.")
            elif not bank_account.isnumeric():
                self.add_error('bank_account', 'Account number must be numeric.')
            if not bank_name:
                self.add_error('bank_name', "Bank name is required.")

        elif payment_method == 'UPI':
            upi_id = cleaned_data.get("upi_id")
            if not upi_id:
                self.add_error('upi_id', "UPI ID is required.")
            elif '@' not in upi_id:
                self.add_error('upi_id', 'Invalid UPI ID format.')






    



