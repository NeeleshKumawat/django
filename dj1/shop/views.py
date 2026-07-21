from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to the Shop Page!")


def about(request):
    return HttpResponse("This is the about page of the Shop.")