# Generated by Django 5.0.6 on 2024-06-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_alter_property_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity',
            name='icon',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='amenity',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
