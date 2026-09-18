from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    return render(request, 'home.html')
    context = {
        "name": 'NK',
        "age": 22,
        "skills": ['Python', 'Django', 'React'],
        "user": User('Kumar', 30),
        "blog": {
            "title": 'My First Blog',
            "content": '<b>This is the content of my first blog post.</b>',
            "date_posted": datetime.now(),
        },
        "empty_value": None,
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def blog_details(request):
    post = {
        "title": "Second Template",
        "description": "This is the second template in Django.",
        "author": "NK",
        "created_at": datetime.now(),
        "comments_count": 5,
        "tags": ["Django", "Templates", "Python"],
        "price": 20,
        "number": 10,
    }
    return render(request, 'blog/blog_details.html', {"post": post})

def blog_list(request):
    blogs = [
        {
            "title": "Django Basics",
            "description": "This is the second template in Django.",
            "author": "NK",
            "created_at": datetime.now(),
            "comments_count": 5,
            "tags": ["Django", "Templates", "Python"],
            "price": 20,
            "number": 10,
            "is_featured": False,
        },
        {
            "title": "Third Template",
            "description": "This is the third template in Django.",
            "author": "NK",
            "created_at": datetime.now(),
            "comments_count": 3,
            "tags": ["Django", "Templates", "Python"],
            "price": 25,
            "number": 15,
            "is_featured": True,
        }
    ]

    context = {
        "blogs": blogs,
        "today": datetime.now(),
        "html_code": "<b>Welcome to Django Templates</b>",
    }
    return render(request, 'blog/blog_list.html', context)