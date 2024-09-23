from django.contrib import admin
from .models import Product, Warehouse, TypeOrganization, Organization, Supply

class SupplyAdmin(admin.ModelAdmin):
    list_display = ('Nomenclature', 'Organization', 'Warehouse', 'Product', 'QuantitiProduct', 'Total_price', 'created_at')


admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(TypeOrganization)
admin.site.register(Organization)
admin.site.register(Supply, SupplyAdmin)