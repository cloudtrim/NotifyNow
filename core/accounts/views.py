from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup_page(request):
    return HttpResponse("<h1>This is signup page.</h1>")