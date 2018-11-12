
from django.urls import path
from . import views

urlpatterns = [

    path('', views.inventory, name='inventory'),
    path('create', views.create, name='create'),
    path('<int:inventory_id>', views.detail, name='detail'),
    # path('edit/<int:inventory_id>', views.edit, name='edit'),
    # path('delete/<int:inventory_id>', views.delete, name='delete'),
]
