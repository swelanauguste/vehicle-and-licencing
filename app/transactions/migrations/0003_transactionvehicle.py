# Generated by Django 5.0.6 on 2024-06-15 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0001_initial'),
        ('transactions', '0002_transactioninsurance_transactionlicence'),
        ('vehicles', '0002_vehicle_owners'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_paid', models.DateField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=100.0, max_digits=10)),
                ('receipt_number', models.CharField(max_length=255, unique=True)),
                ('paid_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='offices.location')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicles', to='transactions.transactiontype')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.vehicle')),
            ],
        ),
    ]