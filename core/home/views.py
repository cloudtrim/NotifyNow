from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    print("you are in dashboard view in home")
    return render(request, "dashboard.html")
    