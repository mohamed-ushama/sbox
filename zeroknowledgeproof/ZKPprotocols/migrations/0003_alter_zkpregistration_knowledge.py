# Generated by Django 4.0.7 on 2023-12-09 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZKPprotocols', '0002_rename_spregistration_zkpregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zkpregistration',
            name='knowledge',
            field=models.CharField(max_length=200),
        ),
    ]