# Generated by Django 5.0.6 on 2024-07-01 13:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_remove_property_pets_allowed'),
        migrations.swappable_dependency(settings.STAR_RATINGS_RATING_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.STAR_RATINGS_RATING_MODEL),
        ),
    ]
