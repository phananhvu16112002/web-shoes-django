# Generated by Django 4.1.2 on 2022-10-29 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_product_image_productattribute_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productattribute',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product_imgs/'),
        ),
    ]
