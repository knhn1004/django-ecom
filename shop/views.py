from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(req):

    text = 'Hello World'
    return HttpResponse(text)
