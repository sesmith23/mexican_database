# Generated by Django 5.0 on 2023-12-04 23:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("geo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="location",
            options={
                "verbose_name": "Geographic Location",
                "verbose_name_plural": "Geographic Locations",
            },
        ),
        migrations.RemoveField(
            model_name="location",
            name="value",
        ),
    ]
