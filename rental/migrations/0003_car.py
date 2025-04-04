# Generated by Django 5.1.7 on 2025-03-15 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_carowner_rename_mobile_user_mobile_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('number_plate', models.CharField(max_length=20, unique=True)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('daily_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('with_driver', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Booked', 'Booked')], default='Available', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.carowner')),
            ],
        ),
    ]
