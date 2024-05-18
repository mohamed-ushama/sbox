from django.db import models

# Create your models here.
class SPregistration(models.Model):

    companyname=models.CharField(max_length=20,null=True)
    contactperson = models.CharField(max_length=20,null=True)
    emailid=models.EmailField(unique=True)
    industry = models.CharField(max_length=20, null=True)
    serviceoffer=models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=10,null=True)
    spid= models.CharField(max_length=10,null=True)

    password=models.CharField(max_length=20)
    approve = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    login = models.BooleanField(default=False)
    logout = models.BooleanField(default=True)

    accept = models.BooleanField(default=False)
    request = models.BooleanField(default=False)

    contract=models.BooleanField(default=True)
    negotiation=models.BooleanField(default=True)


    companyname = models.CharField(max_length=200,null=True)
    companyemailid = models.EmailField(unique=True, null=True)
    duration = models.CharField(max_length=200,null=True)
    industry = models.CharField(max_length=200,null=True)
    serviceneeded = models.CharField(max_length=100,null=True)
    budget = models.CharField(max_length=20, null=True)
    SLA = models.CharField(max_length=200, null=True)
    DataSecurity = models.CharField(max_length=200, null=True)
    IPownership = models.CharField(max_length=200, null=True)
    DisputeResolution = models.CharField(max_length=200,null=True)
    TerminationClauses = models.CharField(max_length=200,null=True)
    NegotiationPoints = models.CharField(max_length=200,null=True)
    DesiredOutcomes = models.CharField(max_length=200,null=True)
    ClauseRational = models.CharField(max_length=200,null=True)
    Ntime = models.CharField(max_length=200,null=True)
    contractlength = models.CharField(max_length=200, null=True)

    agree = models.BooleanField(default=False)
    reject= models.BooleanField(default=False)
    sendntimeoutsourcees=models.BooleanField(default=False)
    zkpprotocol=models.CharField(max_length=200,null=True)
    Outscomply=models.BooleanField(default=False)
    spcomply = models.BooleanField(default=False)
    zkpadminapprove = models.BooleanField(default=False)
    zkpadminreject = models.BooleanField(default=False)
    contractapprov=models.BooleanField(default=False)
    contractreject = models.BooleanField(default=False)
    zkpidentifier= models.CharField(max_length=20,null=True)
    fileupload1 = models.FileField(upload_to='documents/',default=None)
    key=models.BinaryField(max_length=100, null=True)
    leakdata=models.BooleanField(default=False,null=True)
    sendtooutsoucees=models.BooleanField(default=False,null=True)
    complaint=models.CharField(max_length=200,null=True)
    solution=models.CharField(max_length=200,null=True)
    leakcontent=models.CharField(max_length=200,null=True)
    sendsolution = models.BooleanField(default=False)
    inspect = models.BooleanField(default=False)

