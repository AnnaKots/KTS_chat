from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')
# Create your views here.
# Ищет в templates