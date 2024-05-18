from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from outsourcingportal.models import comprequirement
from serviceproviders.models import SPregistration

# Create your views here.
def mainpage(request):
    return render(request,"mainpage/home.html")

def outsourceesregister(request):
        if request.method == "POST":
            companyname = request.POST['companyname']
            companyemailid = request.POST['companyemailid']
            contactperson = request.POST['contactperson']
            phoneno = request.POST['phoneno']
            country = request.POST['country']
            password = request.POST['password']
            try:
                outsourceesregistration(companyname=companyname, companyemailid=companyemailid, contactperson=contactperson,
                                 phoneno=phoneno, country=country, password=password).save()
                messages.success(request, " outsourcees registered successfully")
                return render(request, "outsourcees/login.html")
            except:
                messages.info(request, " outsourcees not registered successfully")
        return render(request,"outsourcees/register.html")

def outsourceeslogin(request):
    if request.method == 'POST':
        companyemailid = request.POST.get('companyemailid')
        password = request.POST.get('password')

        try:
            outsourcees= outsourceesregistration.objects.get(companyemailid=companyemailid, password=password)

            if outsourcees.approve:
                messages.info(request, "outsourcees Login Successful")
                request.session['user_id'] = outsourcees.id
                print(request.session['user_id'])
                outsourcees.login = True
                outsourcees.logout = False
                outsourcees.save()
                return redirect("/outsourcehome/")
            else:
                messages.info(request, "outsourcees need management approval to access")
                return render(request, "outsourcees/login.html")

        except outsourceesregistration.DoesNotExist:
            messages.info(request, " outsourcees enter Invalid Email or Password")

    return render(request,"outsourcees/login.html")

def outsourceeslogout(request):
        if 'user_id' in request.session:
            user_id = request.session.get('id')
            try:
                 outsourcees= outsourceesregistration.objects.get(id=user_id)
                 outsourcees.logout = True
                 outsourcees.login = False
                 outsourcees.save()
                 del request.session['user_id']
                 return redirect('/mainpg/')
            except outsourceesregistration.DoesNotExist:
                request.session.pop('user_id', None)
                messages.error(request, 'outsourcees not found')
        else:
            messages.info(request, 'You are already logged out')

        return redirect('/mainpg/')

def outsourceeshome(request):
    return render(request,"outsourcees/home.html")


def viewcompanies(request):
    viewall=comprequirement.objects.all()
    data = {'data': viewall}
    return render(request, 'outsourcees/viewcomp.html', context=data)

def viewSP(request):
    viewall=SPregistration.objects.all()
    data = {'data': viewall}
    return render(request, 'outsourcees/viewSP.html', context=data)


def ntimeoutsoourcees(request):
    outsourceesid= request.session.get("user_id")
    if outsourceesid:
        data = outsourceesregistration.objects.filter(id=outsourceesid)
        data1 = SPregistration.objects.filter(sendntimeoutsourcees=True)
        return render(request, 'outsourcees/viewnegotime.html',{'data': data,'data1':data1})
    else:
        messages.error(request, "User session not found.")
    return redirect("/outsourcehome/")


def viewspdata(request):
    data = SPregistration.objects.filter(sendtooutsoucees=True)
    return render(request, 'outsourcees/viewspdata.html', {'data': data})


def spcomplaint(request):
    data = SPregistration.objects.filter(sendtooutsoucees=True,leakdata=True)
    return render(request, 'outsourcees/spcomplaint.html', {'data': data})

def makecomplaintsp(request,id):
    data = SPregistration.objects.get(id=id)

    if data.industry=="Technology":
        data.complaint="Intrusion on employee privacy and potential misuse of location data for surveillance."
        data.leakcontent="Misconfigured tracking software; unauthorized data sharing with third parties."
    if data.industry=="Finance":
        data.complaint="Increased risk of unauthorized financial transactions and potential insider trading by hackers."
        data.leakcontent = "Data breach at a data analytics platform; compromised API integration with financial institutions."
    if data.industry=="Manufacturing":
        data.complaint="Potential product safety risks due to leaked testing data and customer complaints."
        data.leakcontent = "System misconfiguration, unauthorized data access by third-party vendors."
    if data.industry=="Healthcare":
        data.complaint="Unintended exposure of diagnoses, medications, and personal health information"
        data.leakcontent = "Data breach at a scheduling platform; unauthorized access by third-party."
    if data.industry=="Retail":
        data.complaint="Intrusion on customer privacy and potential misuse of browsing history."
        data.leakcontent = "Targeted marketing campaigns based on leaked purchase history; spam calls and emails."
    if data.industry=="Legal Services":
        data.complaint="Potential harm to client cases due to leaked witness statements and confidential legal strategies."
        data.leakcontent = "Unsecured document storage; data breach at a cloud storage provider."
    if data.industry=="Education":
        data.complaint="Potential for unfair academic advantage and copyright infringement due to leaked learning materials."
        data.leakcontent = "Platform vulnerability, data scraping by unauthorized individuals."
    if data.industry=="Media & Entertainment":
        data.complaint="Potential identity theft and unauthorized access to personal preferences and financial information."
        data.leakcontent = "Data breach at a collaboration platform, unauthorized access by competitors."
    data.save()
    messages.info(request, 'complaint done successfully')
    return redirect("/outsourcehome/")
