from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'login.html')


def adminuser(request):
    return render(request, 'admin.html')


def signup(request):
    return render(request, 'signup.html')

def personaluser(request):
    return render(request, './shop/index.html')


def addCatelog(request):
    return HttpResponse("addCatelog")


def changePrice(request):
    return HttpResponse("ChangePrice")
