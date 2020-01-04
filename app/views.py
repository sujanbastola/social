from django.shortcuts import render
from django.core.mail import send_mail




# Create your views here.
def home(request):
    return render(request, 'suru/home.html',)
def go(request):
    return render(request, 'suru/ss.html',)
def contact(request):

    return render(request, 'suru/contact.html',)
