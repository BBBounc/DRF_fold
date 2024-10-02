# storage/views.py
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from rest_framework import viewsets
from .serializers import SupplySerializer

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

def add_all(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'product':
            form = ProductForm(request.POST)
        elif form_type == 'warehouse':
            form = WarehouseForm(request.POST)
        elif form_type == 'organization':
            form = OrganizationForm(request.POST)
        elif form_type == 'type_organization':
            form = TypeOrganizationForm(request.POST)
        elif form_type == 'supply':
            form = SupplyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_all')
    else:
        product_form = ProductForm()
        warehouse_form = WarehouseForm()
        organization_form = OrganizationForm()
        type_organization_form = TypeOrganizationForm()
        supply_form = SupplyForm()

    context = {
        'product_form': product_form,
        'warehouse_form': warehouse_form,
        'organization_form': organization_form,
        'type_organization_form': type_organization_form,
        'supply_form': supply_form,
    }
    return render(request, 'add_all.html', context)

# ---- API ----
class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer