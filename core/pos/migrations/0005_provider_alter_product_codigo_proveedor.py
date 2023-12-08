# Generated by Django 4.2.7 on 2023-11-27 23:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pos", "0004_alter_product_codigo_proveedor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Provider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="Nombre"
                    ),
                ),
                (
                    "desc",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Descripción",
                    ),
                ),
            ],
            options={
                "verbose_name": "Proveedor",
                "verbose_name_plural": "Proveedores",
                "ordering": ["id"],
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="codigo_proveedor",
            field=models.CharField(max_length=50, verbose_name="Codigo proveedor"),
        ),
    ]
