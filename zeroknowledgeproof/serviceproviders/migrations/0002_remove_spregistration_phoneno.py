# Generated by Django 4.0.7 on 2023-12-06 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceproviders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spregistration',
            name='phoneno',
        ),
    ]