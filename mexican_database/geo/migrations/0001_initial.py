# Generated by Django 5.0 on 2023-12-06 00:45

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Poligono",
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
                ("forma", models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="TipoDeLugar",
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
                ("nombre", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "Tipo de Lugar",
                "verbose_name_plural": "Tipos de Lugares",
            },
        ),
        migrations.CreateModel(
            name="Lugar",
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
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, null=True),
                ),
                ("nombre", models.CharField(max_length=255)),
                ("longitud", models.FloatField(blank=True, null=True)),
                ("latitud", models.FloatField(blank=True, null=True)),
                (
                    "madre",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="hijos",
                        to="geo.lugar",
                        verbose_name="hijo de",
                    ),
                ),
                (
                    "extension_espacial",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="geo.poligono",
                    ),
                ),
                (
                    "tipo_de_lugar",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="type_Lugar",
                        to="geo.tipodelugar",
                        verbose_name="Tipos de Lugar",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lugar",
                "verbose_name_plural": "Lugares",
            },
        ),
    ]
