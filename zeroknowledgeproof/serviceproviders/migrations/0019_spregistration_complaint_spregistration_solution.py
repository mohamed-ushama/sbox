# Generated by Django 4.0.7 on 2023-12-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceproviders', '0018_spregistration_sendtooutsoucees'),
    ]

    operations = [
        migrations.AddField(
            model_name='spregistration',
            name='complaint',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='solution',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
