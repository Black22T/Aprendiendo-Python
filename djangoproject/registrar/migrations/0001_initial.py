# Generated by Django 5.1.4 on 2024-12-25 09:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('nombreCategoria', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nombre de la Categoria')),
                ('descripcionCategoria', models.TextField(blank=True, max_length=250, null=True, verbose_name='Descripcion de la Categoria')),
                ('tipo', models.CharField(choices=[('comestible', 'Comestible'), ('no_comestible', 'No Comestible')], default='comestible', max_length=15, verbose_name='Tipo de Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('nombreMarca', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nombre de la Marca')),
                ('descripcionMarca', models.TextField(blank=True, max_length=250, null=True, verbose_name='Descripcion de la Marca')),
            ],
        ),
        migrations.CreateModel(
            name='subcategoria',
            fields=[
                ('nombreSubcategoria', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nombre de la Subcategoria')),
                ('descripcionSubcategoria', models.TextField(blank=True, max_length=250, null=True, verbose_name='Descripcion de la Subcategoria')),
                ('tipo', models.CharField(choices=[('retornable', 'Retornable'), ('descartable', 'Descartable')], default='descartable', max_length=15, verbose_name='Tipo de subCategoria')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='registrar.categoria', verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigoBarra', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID del Producto')),
                ('nombreProducto', models.CharField(blank=True, max_length=50, verbose_name='Nombre del Producto')),
                ('fechaIngreso', models.DateField(blank=True, verbose_name='Fecha de Ingreso')),
                ('fechaVencimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Vencimiento')),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Precio')),
                ('contenido', models.IntegerField(blank=True, null=True, verbose_name='Contenido')),
                ('cantidad', models.IntegerField(blank=True, null=True, verbose_name='Cantidad')),
                ('descripcion', models.TextField(blank=True, max_length=250, null=True, verbose_name='Descripcion')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos', verbose_name='Imagen')),
                ('Categoria', models.ForeignKey(default='SIN CATEGORIA', on_delete=django.db.models.deletion.CASCADE, to='registrar.categoria')),
                ('marca', models.ForeignKey(default='SIN MARCA', on_delete=django.db.models.deletion.CASCADE, to='registrar.marca')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrar.subcategoria')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaVenta', models.DateTimeField(verbose_name='Fecha y Hora de la Venta')),
                ('ventaRealizada', models.BooleanField(default=False, verbose_name='Venta Realizada')),
                ('usuario', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario que realizó la Venta')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoVendido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(verbose_name='Cantidad Vendida')),
                ('precioAlMomento', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Precio al momento de la Venta')),
                ('producto', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='registrar.producto', verbose_name='Producto')),
                ('venta', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='productosVendidos', to='registrar.venta', verbose_name='Venta')),
            ],
        ),
    ]
