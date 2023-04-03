from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from math import ceil
import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.

def test(request):
    allProds = []
    catprods = Product.objects.values('sub_category', 'id')
    cats = {item['sub_category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(sub_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    allcustomer = Customer.objects.filter()
    cust = allcustomer[0]
    params = {'allProds': allProds, 'customer': cust}
    return render(request, 'shop/index.html', params)


def index(request,user1_id):
    allProds = []
    catprods = Product.objects.values('sub_category','id')
    cats = {item['sub_category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(sub_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    allcustomer = Customer.objects.filter()
    cust = None
    for i in allcustomer:
        if i.user.id == user1_id:
            cust = i
    params = {'allProds': allProds,'customer':cust}
    return render(request, 'shop/index.html', params)

def about(request,user1_id):
    allcustomer = Customer.objects.filter()
    cust = None
    for i in allcustomer:
        if i.user.id == user1_id:
            cust = i
    return render(request, 'shop/about.html',{'customer': cust})


def contact(request,user1_id):
    allcustomer = Customer.objects.filter()
    cust = None
    for i in allcustomer:
        if i.user.id == user1_id:
            cust = i
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html', {'customer': cust})


def learn(request):
    return render(request, 'shop/learn.html')

def tracker(request):
    return render(request, 'shop/tracker.html')


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("This is not a customer id")
            else:
                return index(request,user.id)
        else:
            alert = True
            return render(request, "shop/login.html", {'alert': alert})
    return render(request, "shop/login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match")

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        customer = Customer.objects.create(user=user, first_name=first_name, last_name=last_name, email=email,
                                           phone=phone)
        user.save()
        customer.save()

        return log_in(request)
    return render(request, "shop/signup.html")



def search(request):
    return render(request, 'search.html')


def productView(request, id,user1_id):
    # Fetch the product using the id
    product = Product.objects.filter(id=id)
    allcustomer = Customer.objects.filter()
    cust = None
    for i in allcustomer:
        if i.user.id == user1_id:
            cust = i

    return render(request, 'shop/prodView.html', {'product': product[0], 'customer': cust})


def checkout(request,user1_id):
    allcustomer = Customer.objects.filter()
    cust = None
    for i in allcustomer:
        if i.user.id == user1_id:
            cust = i
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')[1:-1]
        p = items_json.split('"')
        j = 0
        item_id, item_number = 0, 0
        for i in p:
            
            if (j % 4 == 1):
            # item id
                item_id = int(i[2:])
            if (j % 4 == 2):
            # item number
                item_number=int(i[2:-1])
            if (j % 4 == 3):
                allpro=Product.objects.filter()
                pro=None
                for k in allpro:
                    if item_id==k.id:
                        pro=k
                order1 = OrderDetail.objects.create(order_name=pro.product_name, customer_id=cust.user.id,customer_name=cust.user.username,
                                                    product_id=pro.id, product_taken=item_number, sub_cat=pro.sub_category, total_price=pro.price*item_number)
                cust.changeMaxLoan(pro.price*item_number)
                cust.changePendingAmount(pro.price*item_number)
                cust.save()
                pro.changePrice(item_number)
                pro.changeCurrentNumber(item_number)
                pro.save()
                order1.save()
            j += 1
        return render(request, 'shop/checkout.html', {'customer': cust, 'thank': True})

    return render(request, "shop/checkout.html", {'customer': cust})


def history(request, user1_id):
    allcustomer = Customer.objects.filter()
    cust = None
    for i in allcustomer:
        if i.user.id == user1_id:
            cust = i
    all_order = OrderDetail.objects.filter(customer_id=user1_id)
    return render(request,"shop/history.html",{'orders':all_order,'customer':cust})


def explore(request):
    allProds = []
    catprods = Product.objects.values('sub_category', 'id')
    cats = {item['sub_category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(sub_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/demoview.html', params)


def profile(request,user1_id):
    allcustomer = Customer.objects.filter()
    cust = None
    for i in allcustomer:
        if i.user.id == user1_id:
            cust = i
    all_order = OrderDetail.objects.filter(customer_id=user1_id)
    return render(request,"shop/profile.html",{'customer':cust,'OrderDetail':all_order})