from django.shortcuts import render,redirect
from .models import *

def index(request):
  return render(request, 'index.html')  



def information(request):
    products = Product.objects.all()
    warehouses = Warehouse.objects.all()
    type_organizations = TypeOrganization.objects.all()
    organizations = Organization.objects.all()
    supplies = Supply.objects.all()
    context = {
        'tovar': products,
        'sklad': warehouses,
        'TypeOrg': type_organizations,
        'organization': organizations,
        'postavka': supplies
    }
    return render(request, 'information.html', context)  