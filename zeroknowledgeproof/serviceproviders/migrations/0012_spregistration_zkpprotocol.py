# Generated by Django 4.0.7 on 2023-12-12 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceproviders', '0011_spregistration_sendntimeoutsourcees'),
    ]

    operations = [
        migrations.AddField(
            model_name='spregistration',
            name='zkpprotocol',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
