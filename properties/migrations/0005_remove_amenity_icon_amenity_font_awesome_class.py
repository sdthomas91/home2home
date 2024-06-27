# Generated by Django 5.0.6 on 2024-06-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_alter_amenity_icon_alter_amenity_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amenity',
            name='icon',
        ),
        migrations.AddField(
            model_name='amenity',
            name='font_awesome_class',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
