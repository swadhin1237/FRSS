# Generated by Django 4.1.7 on 2023-04-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_product_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone_number', models.IntegerField(default='')),
                ('address', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('zip_code', models.IntegerField(default='')),
                ('credit_card_number', models.IntegerField(default='')),
                ('month', models.CharField(default='', max_length=15)),
                ('year', models.DateField(default='')),
                ('cvv', models.IntegerField(default='')),
            ],
        ),
    ]