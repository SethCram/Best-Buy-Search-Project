# -*- coding: utf-8 -*-

from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.db import transaction

from .models import Vendor, User, Customer, VendorProduct
#from django.contrib.auth.models import User

class CustomerSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        """Signup redef'd user."""
        model = User
        
    @transaction.atomic
    def save(self, commit = True):
        """
            Atomically save user as customer.
            Can override to not commit save.
        """
        user = super().save(commit = False)
        user.is_customer = True
        if (commit):
            user.save()
        #create new customer: 
        customer = Customer.objects.create(user = user)
        return user
    
class VendorSignUpForm(UserCreationForm):
    """Add brand name field to default vendor sign up."""
    brand = forms.CharField(required = True)
    
    class Meta(UserCreationForm.Meta):
        """Signup redef'd user."""
        model = User
        
    @transaction.atomic
    def save(self):
        """
            Atomically save user as vendor.
        """
        user = super().save(commit = False)
        user.is_vendor = True
        user.save()
        #make sure brand data saved by adding entry: 
        vendor = Vendor.objects.create(user = user, brand = self.cleaned_data['brand'])
        return user

class ProductForm(forms.ModelForm):
    
    #override cost input to be options
    ANY = 1
    LT_50 = 2
    LT_100 = 3
    LT_500 = 5
    COST_CHOICES = (
        (ANY, "Any"),
        (LT_50, "< $50"),
        (LT_100, "< $100"),
        (LT_500, "< $500"),
    )
    cost = forms.ChoiceField(choices = COST_CHOICES)

    class Meta:
        model = VendorProduct
        fields = ['name', 'cost', 'category', 'payment_type']