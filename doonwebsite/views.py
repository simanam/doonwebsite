from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Inventory
from django.utils import timezone

# Create your views here.
def home(request):

    return render(request, 'doonwebsite/home.html')


def inventory(request):
    inventorys = Inventory.objects
    return render(request, 'doonwebsite/inventory.html',{'inventorys':inventorys})

@login_required(login_url="/accounts/login")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['brand']  and request.FILES['image']:
            inventory = Inventory()
            inventory.title = request.POST['title']
            inventory.brand = request.POST['brand']
            inventory.body = request.POST['body']
            inventory.image = request.FILES['image']
            inventory.pub_date = timezone.datetime.now()
            inventory.adder = request.user
            inventory.save()
            return redirect('/inventory/'+ str(inventory.id))

        else:
            return render(request, 'doonwebsite/create.html',{'error': 'All fields are required'})

    else:
        return render(request, 'doonwebsite/create.html')

def detail(request, inventory_id):
    inventory = get_object_or_404(Inventory, pk=inventory_id)

    return render(request, 'doonwebsite/detail.html', {'inventory':inventory})

# def edit(request, inventory_id):
#     if request.method == 'POST':
#         inventory = get_object_or_404(Inventory, pk=inventory_id)
#         inventory.title = request.POST['title']
#         inventory.brand = request.POST['brand']
#         inventory.body = request.POST['body']
#         inventory.image = request.FILES['image']
#         inventory.save()
#         return redirect('/inventorys/'+ str(inventory.id))
#
# def delete(request, inventory_id):
#     inventory = get_object_or_404(Inventory, pk=inventory_id)
#     inventory.delete()
#     inventory.save()
#
#     return redirect('/inventory/')
