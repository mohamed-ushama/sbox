# Generated by Django 4.0.7 on 2023-12-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceproviders', '0007_spregistration_clauserational_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spregistration',
            name='companyemailid',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
