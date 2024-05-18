from django.db import models

# Create your models here.
class outsourceesregistration(models.Model):
    companyname=models.CharField(max_length=20)
    companyemailid=models.EmailField(unique=True)
    contactperson=models.CharField(max_length=20)
    phoneno=models.PositiveIntegerField()
    country= models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    Ntime = models.CharField(max_length=20,null=True)
    approve = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    login = models.BooleanField(default=False)
    logout = models.BooleanField(default=True)
