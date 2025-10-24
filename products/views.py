from django.shortcuts import render
from django.http import HttpResponse
from .models import productlist

def index(request):
    return render(request,'index.html')


def homepage(request):
    prodlist = productlist.objects.all()
    return render(request,'landing.html',{'prolist':prodlist})


def contactpage(request):
    return render(request, 'contactus.html')


def listpage(request):
    return render(request, 'userslist.html')
