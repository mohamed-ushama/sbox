# Generated by Django 4.0.7 on 2024-04-25 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsourcingportal', '0002_comprequirement_fileupload1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compregistration',
            name='companyname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='compregistration',
            name='contactperson',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='comprequirement',
            name='companyname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='comprequirement',
            name='contactperson',
            field=models.CharField(max_length=25),
        ),
    ]