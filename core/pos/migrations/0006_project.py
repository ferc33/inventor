# Generated by Django 4.2.7 on 2023-12-01 01:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pos", "0005_provider_alter_product_codigo_proveedor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("nombre", models.CharField(max_length=200, verbose_name="Nombre")),
                ("fecha_inicio", models.DateField()),
                ("fecha_fin_estimada", models.DateField()),
                (
                    "encargado",
                    models.CharField(max_length=200, verbose_name="Encargado"),
                ),
            ],
            options={
                "verbose_name": "Proyecto",
                "verbose_name_plural": "Proyectos",
                "ordering": ["nombre"],
            },
        ),
    ]
