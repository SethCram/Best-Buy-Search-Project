from datetime import datetime
from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
import random
import faker_commerce

from django.utils import timezone

from BestBuySearch.models import VendorProduct, User, Customer, Vendor 

class ExtraProvider(faker.providers.BaseProvider):
    def category(self):
        return self.random_element(VendorProduct.CATEGORY)

    def payment_type(self):
        return self.random_element(VendorProduct.PAYMENT_TYPE)

class Command( BaseCommand ):
    help = "Command information"

    def handle(self, *args, **kwargs):
        """Function called w/ command run."""
        #print("hello")

        NUM_OF_PRODS = 2

        #init faker
        fake = Faker()
        fake.add_provider(ExtraProvider)
        fake.add_provider(faker_commerce.Provider)

        #print(fake.category())

        print("before faking num of prods: ", VendorProduct.objects.all().count() )

        #create new vendor to link to created prods

        usernameRando = fake.user_name()
        brandRando = fake.word()
        usr = User.objects.create_user(username=usernameRando, password="test", is_vendor=1)
        vendor = Vendor.objects.get_or_create(user_id=usr.id, brand=brandRando)

        #create specified num of prods
        for _ in range(NUM_OF_PRODS):

            #id = faker.random.uuid()
            #username = faker.internet.userName()

            name = fake.ecommerce_name() #fake.word()
            cost = fake.ecommerce_price() #round(random.uniform(0.00, 1000.99), 2) #gens str: fake.pricetag() 
            #debug: print("cost:", cost)
            category = fake.random_int(1, 20)
            quantity = fake.random_int(1, 1000)
            payment_type = fake.random_int(1,2)
            prod_descr = fake.paragraph(nb_sentences=3)
            brief_descr = fake.text(max_nb_chars=20)
            #don't actually work for display
            small_image = fake.image_url()
            big_image = fake.image_url()

            update_date = timezone.now() #tuple: fake.date_this_decade()
            pub_date = fake.date_this_decade()

            #update and pub date should be added w/ saving create prods
            #won't "created_by" be added too?

            VendorProduct.objects.create(
                #created_by=user, #created_by,
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




