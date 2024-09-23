from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(TypeOrganization)
admin.site.register(Organization)
admin.site.register(Supply)