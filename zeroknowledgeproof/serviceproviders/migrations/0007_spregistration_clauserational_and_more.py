# Generated by Django 4.0.7 on 2023-12-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceproviders', '0006_spregistration_accept_spregistration_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='spregistration',
            name='ClauseRational',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='DataSecurity',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='DesiredOutcomes',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='DisputeResolution',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='IPownership',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='NegotiationPoints',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='Ntime',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='SLA',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='TerminationClauses',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='agree',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='budget',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='duration',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spregistration',
            name='serviceneeded',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spregistration',
            name='companyname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='spregistration',
            name='contactperson',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='spregistration',
            name='industry',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='spregistration',
            name='location',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='spregistration',
            name='serviceoffer',
            field=models.CharField(max_length=100, null=True),
        ),
    ]