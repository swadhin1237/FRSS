# Generated by Django 4.1.7 on 2023-04-03 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_payment_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('product_id', models.IntegerField(default=0)),
                ('user_review', models.CharField(default='', max_length=500)),
                ('user_name', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
