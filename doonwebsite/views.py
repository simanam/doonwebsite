from django.shortcuts import render, redirect

# Create your views here.
def home(request):

    return render(request, 'doonwebsite/home.html')


def inventory(request):

    return render(request, 'doonwebsite/inventory.html')
