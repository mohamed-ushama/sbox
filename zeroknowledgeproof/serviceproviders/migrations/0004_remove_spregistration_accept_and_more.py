# Generated by Django 4.0.7 on 2023-12-07 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceproviders', '0003_spregistration_accept_spregistration_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spregistration',
            name='accept',
        ),
        migrations.RemoveField(
            model_name='spregistration',
            name='request',
        ),
    ]