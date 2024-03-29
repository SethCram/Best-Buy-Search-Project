from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
import faker.providers
import random
import faker_commerce
import requests
from django.conf import settings

from django.utils import timezone

from BestBuySearch.models import VendorProduct, User, Customer, Vendor 

class ExtraProvider(faker.providers.BaseProvider):
    """Adds an extra, user defined provider to faker."""
    def category(self):
        return self.random_element(VendorProduct.CATEGORY)

    def payment_type(self):
        return self.random_element(VendorProduct.PAYMENT_TYPE)

class Command( BaseCommand ):
    """
    Generates products and a vendor who created them.
    Requires a number of products to create as an arg.
    """
    help = "Creates test data for BestBuySearch products."

    def add_arguments(self, parser):
        """Add an additional arg to run command."""
        parser.add_argument('number_of_products', type=int)
        
    def fakeImage(self, fake: Faker, width: int, height: int) -> str:
        """Fake image through getting one off the internet, 
        saving it to the images folder in media,
        and returning the image name.

        Args:
            fake (Faker): faker instance for genning fake data

        Returns:
            str: image name beginning with /images/ 
        """
        
        #gen url
        small_img_url = fake.image_url(width, height)
        #get img off internet
        img = requests.get(small_img_url)
        #construct img name
        imgName = "/images/" + f"{fake.word()}_fake.png"
        #construct img path
        imgPath = settings.MEDIA_ROOT + imgName
        
        #save to file in media folder
        with open(imgPath, "wb") as file:
            file.write(img.content)
            
        return imgName

    def handle(self, *args, **kwargs):
        """
        Function calls w/ command runs to generate 
            products and a vendor who created them.
        Requires a number of products to create as an arg.
        """

        NUM_OF_PRODS = kwargs['number_of_products']

        #init faker
        fake = Faker()
        fake.add_provider(ExtraProvider)
        fake.add_provider(faker_commerce.Provider)

        print("before faking num of prods: ", VendorProduct.objects.all().count() )

        #create new vendor to link to created prods

        usernameRando = fake.user_name()
        brandRando = fake.word()
        usr = User.objects.create_user(username=usernameRando, password="test", is_vendor=1)
        vendor = Vendor.objects.get_or_create(user_id=usr.id, brand=brandRando)

        #create specified num of prods
        for _ in range(NUM_OF_PRODS):

            name = fake.ecommerce_name() #+ " (fake)" #fake.word()
            cost = round(random.uniform(0.00, 10000.99), 2) #fake.ecommerce_price() #gens str: fake.pricetag() 
            #debug: print("cost:", cost)
            category = fake.random_int(1, len(VendorProduct.CATEGORY)) #goes up to 20 rn
            quantity = fake.random_int(1, 1000)
            payment_type = fake.random_int(1, len(VendorProduct.PAYMENT_TYPE)) #goes up to 20 rn
            prod_descr = fake.paragraph(nb_sentences=3)
            brief_descr = fake.text(max_nb_chars=20)
            #won't actually work to display images bc looking in media folder
            
            #fake imgs
            small_image = self.fakeImage(fake, width=450, height=300)
            big_image = self.fakeImage(fake, width=600, height=700)

            update_date = timezone.now() #tuple: fake.date_this_decade()
            pub_date = fake.date_this_decade()

            VendorProduct.objects.create(
                name=name,
                cost=cost,
                category=category,
                quantity=quantity,
                payment_type=payment_type,
                product_description=prod_descr,
                brief_description=brief_descr,
                small_display_image=small_image,
                big_display_image=big_image,
                update_date=update_date,
                pub_date = pub_date,
                created_by=usr
            )

            #print(cost, category)
        
        print("after faking num of prods: ", VendorProduct.objects.all().count() )
