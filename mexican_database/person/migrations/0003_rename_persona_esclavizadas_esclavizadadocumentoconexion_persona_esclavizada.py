# Generated by Django 5.0 on 2023-12-06 00:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("person", "0002_remove_esclavizadordocumentoconexion_persona_altura_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="esclavizadadocumentoconexion",
            old_name="persona_esclavizadas",
            new_name="persona_esclavizada",
        ),
    ]
