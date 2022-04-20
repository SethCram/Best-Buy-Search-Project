# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:02:40 2022

@author: crazy
"""

from django.contrib import admin

class MyAdminSite(admin.AdminSite):    
    site_header = "Product Administration"
    
    site_title = "Vendor site admin"

    site_url = "/BestBuySearch/" #override field w/ instance

    #redirects unauthenticated users to the login page. By default, it is set to True.
    #final_catch_all_view = False #Setting this to False is not recommended as the view protects against a potential model enumeration privacy issue
    
    #add_url = ""