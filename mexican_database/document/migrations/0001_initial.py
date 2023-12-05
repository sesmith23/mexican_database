# Generated by Django 5.0 on 2023-12-04 23:47

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("geo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Asunto",
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
                    "nombre",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        verbose_name="Geographic Location Type",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Documento",
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
                    "day",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(31),
                        ],
                    ),
                ),
                (
                    "month",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(12),
                        ],
                    ),
                ),
                (
                    "year",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(2000),
                        ],
                    ),
                ),
                (
                    "folio",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        unique=True,
                        verbose_name="Folio",
                    ),
                ),
                (
                    "vol",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        unique=True,
                        verbose_name="Folio",
                    ),
                ),
                (
                    "resumen",
                    models.CharField(
                        blank=True, max_length=250, null=True, verbose_name="Resumen"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Archivo",
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
                        blank=True,
                        max_length=20,
                        null=True,
                        unique=True,
                        verbose_name="Archive name",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="archives",
                        to="geo.location",
                        verbose_name="Archive Location",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Fondo",
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
                    "archivo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="fondos",
                        to="document.archivo",
                        verbose_name="Archivo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubFondo",
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
                    "fondo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="subfondos",
                        to="document.fondo",
                        verbose_name="Fondo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Volume",
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
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="children",
                        to="document.volume",
                        verbose_name="Child of",
                    ),
                ),
            ],
        ),
    ]
