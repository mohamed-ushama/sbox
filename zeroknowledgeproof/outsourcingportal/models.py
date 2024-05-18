from django.db import models

# Create your models here.
class compregistration(models.Model):
    companyname=models.CharField(max_length=50)
    companyemailid=models.EmailField(unique=True)
    contactperson=models.CharField(max_length=25)
    phoneno=models.PositiveIntegerField()
    country= models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    approve = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    login = models.BooleanField(default=False)
    logout = models.BooleanField(default=True)
    process = models.BooleanField(default=False)
    upload = models.BooleanField(default=False)

class comprequirement(models.Model):
    companyname=models.CharField(max_length=50)
    contactperson=models.CharField(max_length=25)
    companyemailid = models.EmailField(unique=False,null=True)
    location= models.CharField(max_length=10)
    industry=models.CharField(max_length=20,null=True)
    serviceneed=models.CharField(max_length=200)
    duration=models.CharField(max_length=20,null=True)
    budget = models.CharField(max_length=20, null=True)
    accept = models.BooleanField(default=False)
    request = models.BooleanField(default=False)
    fileupload1 = models.FileField(upload_to='documents/', default=None)

class myresource(models.Model):
    companyname = models.CharField(max_length=20, null=True)
    contactperson = models.CharField(max_length=20, null=True)
    companyemailid = models.EmailField(unique=True, null=True)
    fileupload1 = models.FileField(upload_to='documents/')
    FullName = models.CharField(max_length=20,null=True)
    DateofBirth = models.CharField(max_length=20,null=True)
    Gender = models.EmailField(unique=True, null=True)
    Address = models.CharField(max_length=10,null=True)
    Phone = models.CharField(max_length=20, null=True)
    Insurance = models.CharField(max_length=200,null=True)
    DiagnosisName = models.CharField(max_length=20, null=True)
    ProcedureName = models.CharField(max_length=20, null=True)




