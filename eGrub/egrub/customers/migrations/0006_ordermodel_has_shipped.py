# Generated by Django 3.2.23 on 2024-01-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_ordermodel_has_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='has_shipped',
            field=models.BooleanField(default=False),
        ),
    ]
