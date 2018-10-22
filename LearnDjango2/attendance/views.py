from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'attendance/homepage.html')

def about(request):
    return render(request, 'attendance/about.html')
