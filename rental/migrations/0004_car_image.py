# Generated by Django 5.1.2 on 2025-03-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car_images/'),
        ),
    ]
