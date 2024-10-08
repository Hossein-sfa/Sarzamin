from django.shortcuts import HttpResponse, render
from .models import *


def home(request):
    return render(request, 'home.html')

def contact_us(request):
    return HttpResponse('This is Contact us page')

def about_us(request):
    return HttpResponse('This is About us page')

def add_ticket(request):
    title = request.GET.get('title')
    body = request.GET.get('body')
    if title and body:
        Ticket.objects.create(title=title, body=body)
        return HttpResponse('Ticket created')
    
    return render(request, 'add_ticket.html')