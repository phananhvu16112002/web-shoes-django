# Generated by Django 4.1.2 on 2022-10-27 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_banner_productattribute'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
