# Generated by Django 4.0.7 on 2023-12-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceproviders', '0020_spregistration_leakcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='spregistration',
            name='sendsolution',
            field=models.BooleanField(default=False),
        ),
    ]