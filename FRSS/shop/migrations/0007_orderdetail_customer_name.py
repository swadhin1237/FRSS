# Generated by Django 4.1.7 on 2023-04-02 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderdetail_product_totalnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='customer_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
