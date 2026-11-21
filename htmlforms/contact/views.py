from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact


def contact_form(request):
    return render(request, 'contact.html')


def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message= request.POST.get('message')

        if name and message:
            Contact.objects.create(name=  name, message = message)
            return HttpResponse(f"Thank Youm {name}, for your message")
        else:
            return HttpResponse(F"PLEASE PROVIDE BOTH NAME AND MESSAGE")
        
    return redirect('contact_form')

