# Generated by Django 4.0.7 on 2023-12-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceproviders', '0004_remove_spregistration_accept_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spregistration',
            name='contract',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='negotiation',
            field=models.BooleanField(default=True),
        ),
    ]
