# Generated by Django 4.0.7 on 2023-12-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceproviders', '0009_alter_spregistration_industry'),
    ]

    operations = [
        migrations.AddField(
            model_name='spregistration',
            name='contractlength',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
