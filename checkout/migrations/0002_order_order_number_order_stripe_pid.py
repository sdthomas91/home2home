# Generated by Django 5.0.6 on 2024-07-03 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default=0, editable=False, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]