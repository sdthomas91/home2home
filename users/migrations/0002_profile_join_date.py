# Generated by Django 5.0.6 on 2024-06-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='join_date',
            field=models.DateField(auto_now_add=True, default='2023-01-01'),
            preserve_default=False,
        ),
    ]