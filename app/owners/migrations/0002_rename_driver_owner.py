# Generated by Django 5.0.6 on 2024-06-15 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Driver',
            new_name='Owner',
        ),
    ]
