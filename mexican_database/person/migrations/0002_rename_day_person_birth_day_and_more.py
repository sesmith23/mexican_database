# Generated by Django 5.0 on 2023-12-05 00:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("person", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="person",
            old_name="day",
            new_name="birth_day",
        ),
        migrations.RenameField(
            model_name="person",
            old_name="month",
            new_name="birth_month",
        ),
        migrations.RenameField(
            model_name="person",
            old_name="year",
            new_name="birth_year",
        ),
        migrations.AddField(
            model_name="person",
            name="death_day",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(31),
                ],
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="death_month",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(12),
                ],
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="death_year",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(2000),
                ],
            ),
        ),
    ]