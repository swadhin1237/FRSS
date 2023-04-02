from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    currentNumber = models.IntegerField(default=25)
    totalNumber = models.IntegerField(default=25)
    product_desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name
    
    def changePrice(self,item_number):
        self.price = self.price-((self.price*0.1*item_number)/self.totalNumber)

    def changeCurrentNumber(self,item_number):
        self.currentNumber = self.currentNumber-item_number


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=10, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=10, default="")
    first_name = models.CharField(max_length=70, default="")
    last_name = models.CharField(max_length=70, default="")
    Pending_amount=models.IntegerField(default=0)
    Max_loan=models.IntegerField(default=0)


    def __str__(self):
        return self.first_name
    
    def changePendingAmount(self, price):
        self.Pending_amount = self.Pending_amount+price

    def changeMaxLoan(self, price):
        self.Max_loan = self.Max_loan+(price*0.3)

class OrderDetail(models.Model):

    order_name = models.CharField(max_length=50,default="")
    customer_id = models.IntegerField(default=0)
    customer_name = models.CharField(max_length=50, default="")
    product_id = models.IntegerField(default=0)
    product_taken = models.IntegerField(default=0)
    sub_cat = models.CharField(max_length=50, default="")
    total_price = models.IntegerField(default=0)
    isPaid=models.BooleanField(default=False)
    isReturn=models.BooleanField(default=False)
    def __str__(self):
        return self.order_name


