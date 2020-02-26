from django.shortcuts import render
from django.http import HttpResponse


def landing_view(request):
    if request.method == 'GET':
        return render(request, 'main.html')


def about_view(request):
    if request.method == 'GET':
        return render(request, "about.html")

def checkout(request):
    if request.method == 'GET':
        return render(request, "checkout.html")

def contacts(request):
    if request.method == 'GET':
        return render(request, "contacts.html")