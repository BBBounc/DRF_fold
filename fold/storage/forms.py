from django import forms
from .models import *
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-input'}),
        }

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name', 'address', 'warehouse_volume']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'address': forms.TextInput(attrs={'class': 'form-input'}),
            'warehouse_volume': forms.NumberInput(attrs={'class': 'form-input'}),
        }

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'type_organization']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'type_organization': forms.Select(attrs={'class': 'form-input'}),
        }

class TypeOrganizationForm(forms.ModelForm):
    class Meta:
        model = TypeOrganization
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
        }

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ['Nomenclature', 'Organization', 'Warehouse', 'Product', 'QuantitiProduct']
        widgets = {
            'Nomenclature': forms.TextInput(attrs={'class': 'form-input'}),
            'Organization': forms.Select(attrs={'class': 'form-input'}),
            'Warehouse': forms.Select(attrs={'class': 'form-input'}),
            'Product': forms.Select(attrs={'class': 'form-input'}),
            'QuantitiProduct': forms.NumberInput(attrs={'class': 'form-input'}),
        }