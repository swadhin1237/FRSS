# Generated by Django 4.1.7 on 2023-04-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_product_totalnumber_product_currentnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='totalNumber',
            field=models.IntegerField(default=25),
        ),
    ]
