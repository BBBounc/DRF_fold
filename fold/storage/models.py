from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    warehouse_volume = models.FloatField()

    def __str__(self):
        return self.name

class TypeOrganization(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=100)
    type_organization = models.ForeignKey(TypeOrganization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Supply(models.Model):
    Nomenclature = models.CharField(max_length=300)
    Organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    Warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    QuantitiProduct = models.PositiveIntegerField()
    Total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)

    def save(self,*args, **kwargs):
        self.Total_price = self.Product.price * self.QuantitiProduct
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Товар: {self.Nomenclature} от {self.Organization.name}"