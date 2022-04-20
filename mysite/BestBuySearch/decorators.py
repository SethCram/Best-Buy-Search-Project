# -*- coding: utf-8 -*-

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def customer_required( function = None, 
                      redirect_field_name = REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the logged in user is a customer,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        #pass test if user is active + customer
        lambda u: u.is_active and u.is_customer,
        login_url = 'login',
        redirect_field_name = redirect_field_name
    )
    
    if function:
        return actual_decorator(function)
    
    return actual_decorator

def vendor_required( function = None, 
                      redirect_field_name = REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the logged in user is a vendor,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        #pass test if user is active + customer
        lambda u: u.is_active and u.is_vendor,
        login_url = 'login',
        redirect_field_name = redirect_field_name
    )
    
    if function:
        return actual_decorator(function)
    
    return actual_decorator
    