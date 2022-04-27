import datetime
from secrets import choice
from unicodedata import category
from unittest.util import _MAX_LENGTH

from django.db import models
from django.utils import timezone

from django.contrib import admin
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.

#query model

"""
class RequirementsQuerySet(models.QuerySet):
    def search(self, **kwargs):
        qs = self
        if kwargs.get('q', ''):
            qs = qs.filter(name__iexact=kwargs['q'])
        if kwargs.get('government_type', []):
            qs = qs.filter(government_type=kwargs['government_type'])
        if kwargs.get('industry', []):
            qs = qs.filter(industry=kwargs['industry'])
        return qs
"""

#User model

class User(AbstractUser):
    """
    Add more fields to default Django User table.
    Adds extra fields common to all users.
    """
    is_vendor = models.BooleanField(default = False)
    is_customer = models.BooleanField(default = False)

#product model

class VendorProduct(models.Model):
    """Item created by vendors and purchased by clients."""
    #VID = models.ForeignKey(Vendor, on_delete = models.CASCADE)
    PID = models.BigAutoField(primary_key = True)
    cost = models.DecimalField(default = 0, max_digits = 20, decimal_places = 2)
    name = models.CharField(max_length = 200)

    #category
    TV_HOME_THEATER = 1
    AUDIO = 2
    MUSICAL_INSTRUMENTS = 3
    CAR_ELECTRONICS_GPS = 4
    CAMERAS_CAMCORDERS_DRONES = 5
    COMPUTERS_TABLETS = 6
    MOVIES_MUSIC = 7
    VIDEO_GAMES = 8
    CELL_PHONES = 9
    APPLIANCES = 10
    GIFT_CARDS = 11
    NAME_BRANDS = 12
    BABY_CARE = 13
    SERVICES = 14
    HEALTH_WELLNESS = 15
    TOYS_GAMES_COLLECTABLES = 16
    SMART_HOME = 17
    SPORTS_FITNESS_RECREATION = 18
    HOME_FURNITURE_OFFICE = 19
    WEARABLE_TECHNOLOGY = 20
    CATEGORY = (
        (TV_HOME_THEATER, "TV & Home Theater"),
        (AUDIO, "Audio"),
        (MUSICAL_INSTRUMENTS, "Musical Instruments" ),
        (CAR_ELECTRONICS_GPS, "Car, Electronics & GPS"),
        (CAMERAS_CAMCORDERS_DRONES, "Cameras, Camcorders & Drone"),
        (COMPUTERS_TABLETS, "Computers & Tablets"),
        (MOVIES_MUSIC, "Movies & Music"),
        (VIDEO_GAMES, "Video Games"),
        (CELL_PHONES, "Cell Phones"),
        (APPLIANCES, "Appliances"),
        (GIFT_CARDS, "Gift Cards"),
        (NAME_BRANDS, "Name Brands"),
        (BABY_CARE, "Baby Care"),
        (SERVICES, "Services"),
        (HEALTH_WELLNESS, "Health & Wellness"),
        (TOYS_GAMES_COLLECTABLES, "Toys, Games & Collectibles"),
        (SMART_HOME, "Smart Home"),
        (SPORTS_FITNESS_RECREATION, "Sports, Fitness & Recreation"),
        (HOME_FURNITURE_OFFICE, "Home, Furniture & Office"),
        (WEARABLE_TECHNOLOGY, "Wearable Technology"),
    )
    category = models.PositiveSmallIntegerField(choices=CATEGORY)

    """#item type
    PRODUCT = 1
    SERVICE = 2
    ITEM_TYPE = (
        (PRODUCT, 'product'),
        (SERVICE, 'service')
    )
    item_type = models.PositiveSmallIntegerField( choices=ITEM_TYPE, default=PRODUCT)
    """
    
    #payment type
    IN_FULL = 1
    MONTHLY = 2
    PAYMENT_TYPE = (
        (IN_FULL, 'in full'),
        (MONTHLY, 'monthly'),
    )
    payment_type = models.PositiveSmallIntegerField( choices=PAYMENT_TYPE, default=IN_FULL)

    quantity = models.PositiveBigIntegerField(default=1)

    #description fields:
    product_description = models.CharField(max_length=200, default='product description...')
    brief_description = models.CharField(max_length=20, default='brief description...')

    #display images (auto uploads to media folder)
    #WIDTH_REQ = 600
    #HEIGHT_REQ = 700
    #small_display_image = models.ImageField(upload_to='images/', width_field=450, height_field=300, max_length=100)
    #big_display_image = models.ImageField(upload_to='images/', width_field=WIDTH_REQ, height_field=HEIGHT_REQ, max_length=100)
    small_display_image = models.ImageField(upload_to='images/', max_length=500)
    big_display_image = models.ImageField(upload_to='images/', max_length=500) 
        #no idea how to restrict the upload resolution

    #dates:
    update_date = models.DateTimeField("date updated")
    pub_date = models.DateTimeField("date published")

    #should include full description field + short description field
    
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Used by CreateView and UpdateView as success_url."""
        #return reverse('add_product', kwargs = {'pk': self.pk})
        return reverse('BestBuySearch:products')
    
#User models

class Customer(models.Model):
    """
    Create profile model via 1-to-1 relations to user model.
    """
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    products = models.ManyToManyField(VendorProduct)
    
    
class Vendor(models.Model):
    """
    Create profile model via 1-to-1 relations to user model.
    """
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    brand = models.CharField(max_length = 200)

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