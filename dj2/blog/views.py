from django.shortcuts import render
from django.http import HttpResponse

def post_details(request, post_id):
    return HttpResponse(f"Details of blog post with ID: {post_id}")

def user_profile(request, username):
    return HttpResponse(f"Profile page of user: {username}")

def article(request, year):
    return HttpResponse(f"Articles from the year: {year}")

# def article_details(request, year, month):
#     return HttpResponse(f"Articles from {month}/{year}")

def article_details(request, **kwargs):
    year = kwargs.get('year')
    month = kwargs.get('month')
    return HttpResponse(f"Articles from {month}/{year}")