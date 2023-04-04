from django.contrib import admin

# Register your models here.
from .models import Product,Customer,Contact,OrderDetail,Payment,Review

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(OrderDetail)
admin.site.register(Payment)
admin.site.register(Review)
