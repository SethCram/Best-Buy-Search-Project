# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:06:29 2022

@author: crazy
"""

from django.contrib.admin.apps import AdminConfig

class MyAdminConfig(AdminConfig):
    default_site = 'mysite.admin.MyAdminSite'