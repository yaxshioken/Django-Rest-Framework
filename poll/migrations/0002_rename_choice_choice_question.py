# Generated by Django 5.1.1 on 2024-09-10 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("poll", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="choice",
            old_name="choice",
            new_name="question",
        ),
    ]
