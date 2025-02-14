# Generated by Django 5.1.3 on 2024-11-16 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('material_id', models.AutoField(primary_key=True, serialize=False)),
                ('material_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'materials',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=10)),
                ('account_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False)),
                ('delivery_date', models.DateField()),
                ('delivery_days', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to='lab.material')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to='lab.supplier')),
            ],
            options={
                'db_table': 'deliveries',
            },
        ),
    ]
