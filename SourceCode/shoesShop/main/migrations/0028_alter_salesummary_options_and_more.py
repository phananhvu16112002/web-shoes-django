# Generated by Django 4.1.2 on 2022-11-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_salesummary_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salesummary',
            options={'verbose_name': 'Revenue', 'verbose_name_plural': 'Revenue'},
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='order_status',
            field=models.CharField(choices=[('Process', 'In Process'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Process', max_length=150),
        ),
    ]
