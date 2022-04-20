import datetime

from django.db import models
from django.utils import timezone

from django.contrib import admin
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.

#User models

class User(AbstractUser):
    """
    Add more fields to default Django User table.
    Adds extra fields common to all users.
    """
    is_vendor = models.BooleanField(default = False)
    is_customer = models.BooleanField(default = False)
    
class Customer(models.Model):
    """
    Create profile model via 1-to-1 relations to user model.
    """
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    
    
    
class Vendor(models.Model):
    """
    Create profile model via 1-to-1 relations to user model.
    """
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    brand = models.CharField(max_length = 200)

#product model

class VendorProduct(models.Model):
    """Item created by vendors and purchased by clients."""
    #VID = models.ForeignKey(Vendor, on_delete = models.CASCADE)
    PID = models.BigAutoField(primary_key = True)
    cost = models.DecimalField(default = 0, max_digits = 20, decimal_places = 2)
    name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    prod_type = models.CharField(max_length = 50)
    payment_type = models.CharField(max_length = 200)
    #dates:
    update_date = models.DateTimeField("date updated")
    pub_date = models.DateTimeField("date published")
    
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Used by CreateView and UpdateView as success_url."""
        #return reverse('add_product', kwargs = {'pk': self.pk})
        return reverse('BestBuySearch:products')



"""#polls models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    
    #needs placed right above function:
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    
    #second ed:
    def was_published_recently(self):
        nowTime = timezone.now()
        
        #ret true if pub_date is less than rn + larger than a day ago's date
        return (nowTime - datetime.timedelta(days=1)) <= self.pub_date <= nowTime
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
"""