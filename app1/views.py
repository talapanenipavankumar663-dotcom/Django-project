from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='color:red'> Hello, welcome to the Django  application!</h1>")