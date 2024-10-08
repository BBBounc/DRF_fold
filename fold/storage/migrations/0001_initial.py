# Generated by Django 5.0.7 on 2024-09-23 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('warehouse_volume', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.typeorganization')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nomenclature', models.CharField(max_length=300)),
                ('QuantitiProduct', models.PositiveIntegerField()),
                ('Total_price', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10)),
                ('Organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.organization')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.product')),
                ('Warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.warehouse')),
            ],
        ),
    ]
