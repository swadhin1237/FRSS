# Generated by Django 4.1.7 on 2023-04-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Max_loan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='Pending_amount',
            field=models.IntegerField(default=0),
        ),
    ]