# Generated by Django 4.0.3 on 2022-04-25 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BestBuySearch', '0004_alter_vendorproduct_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorproduct',
            name='item_type',
        ),
    ]