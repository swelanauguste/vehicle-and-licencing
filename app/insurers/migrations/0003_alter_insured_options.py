# Generated by Django 5.0.6 on 2024-06-15 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurers', '0002_remove_insured_paid_at_insured_date_insured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='insured',
            options={'verbose_name_plural': 'insured'},
        ),
    ]
