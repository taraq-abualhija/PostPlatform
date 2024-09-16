from django.http import HttpResponse
from django.shortcuts import render


def index(req):
    # return HttpResponse('Hello world')
    return render(req, "home.html")


def about(req):
    # return HttpResponse('About page')
    return render(req, "about.html")
