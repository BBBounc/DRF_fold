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

class WarehouseProduct(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} на складе {self.warehouse.name}"

class Supply(models.Model):
    Nomenclature = models.CharField(max_length=300)
    Organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    Warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    QuantitiProduct = models.PositiveIntegerField()
    Total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.Total_price = self.Product.price * self.QuantitiProduct
        super().save(*args, **kwargs)
        warehouse_product, created = WarehouseProduct.objects.get_or_create(
            warehouse=self.Warehouse,
            product=self.Product,
            defaults={'quantity': 0}
        )
        warehouse_product.quantity += self.QuantitiProduct
        warehouse_product.save()

    def __str__(self):
        return f"Товар: {self.Product} от {self.Organization.name}, создан: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"


class Sale(models.Model):
    Nomenclature = models.CharField(max_length=300)
    Organization = models.CharField(max_length=300)
    Warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    QuantitiProduct = models.PositiveIntegerField()
    Total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        warehouse_product = WarehouseProduct.objects.filter(
            warehouse=self.Warehouse,
            product=self.Product
        ).first()

        if warehouse_product is None:
            raise ValueError("Товар отсутствует на складе.")

        if warehouse_product.quantity < self.QuantitiProduct:
            raise ValueError("Товар закончился на складе.")

        self.Total_price = round(self.Product.price * self.QuantitiProduct, 2)
        warehouse_product.quantity -= self.QuantitiProduct
        warehouse_product.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Товар: {self.Product} со склада {self.Warehouse.name}, Продан: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"