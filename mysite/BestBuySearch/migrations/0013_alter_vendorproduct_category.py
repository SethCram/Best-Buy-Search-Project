# Generated by Django 4.0.3 on 2022-04-28 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BestBuySearch', '0012_alter_vendorproduct_big_display_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorproduct',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'TV & Home Theater'), (2, 'Audio'), (3, 'Musical Instruments'), (4, 'Car, Electronics & GPS'), (5, 'Cameras, Camcorders & Drone'), (6, 'Computers & Tablets'), (7, 'Movies & Music'), (8, 'Video Games'), (9, 'Cell Phones'), (10, 'Appliances'), (11, 'Gift Cards'), (12, 'Name Brands'), (13, 'Baby Care'), (14, 'Services'), (15, 'Health & Wellness'), (16, 'Toys, Games & Collectibles'), (17, 'Smart Home'), (18, 'Sports, Fitness & Recreation'), (19, 'Home, Furniture & Office'), (20, 'Wearable Technology')]),
        ),
    ]
