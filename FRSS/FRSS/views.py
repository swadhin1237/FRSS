from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def adminuser(request):
    return render(request, 'admin.html')


def personaluser(request):
    return render(request, 'user.html')


def addCatelog(request):
    return HttpResponse("addCatelog")


def changePrice(request):
    return HttpResponse("ChangePrice")
