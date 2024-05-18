from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from outsourcingportal.models import comprequirement
# Create your views here.
from outsourcingportal.models import compregistration


def mainpage(request):
    return render(request,"mainpage/home.html")

def SPregister(request):
    if request.method == "POST":
        companyname = request.POST['companyname']
        contactperson = request.POST['contactperson']
        emailid = request.POST['emailid']
        industry = request.POST['industry']
        serviceoffer = request.POST['serviceoffer']
        location =request.POST['location']
        password = request.POST['password']
        try:
            SPregistration(companyname=companyname, contactperson=contactperson, emailid=emailid,
                              industry=industry,serviceoffer=serviceoffer, location=location, password=password).save()
            messages.success(request, " Service provider registered successfully")
            return render(request, "Sprovider/login.html")
        except:
            messages.info(request, " Service provider not registered successfully")
            return render(request, "Sprovider/register.html")

    return render(request,"Sprovider/register.html")



def SPlogin(request):
    if request.method == 'POST':
        emailid = request.POST.get('emailid')
        password = request.POST.get('password')

        try:
            SProvider= SPregistration.objects.get(emailid=emailid, password=password)

            if SProvider.approve:
                messages.info(request, "Service provider Login Successful")
                request.session['user_id'] =SProvider.id
                SProvider.login = True
                SProvider.logout = False
                SProvider.save()
                return redirect("/SPhome/")
            else:
                messages.info(request, "Service provider need management approval")
                return render(request,"sprovider/login.html")

        except SPregistration.DoesNotExist:
            messages.info(request, "Service provider enter Invalid Email or Password")

    return render(request,"sprovider/login.html")

def SPlogout(request):
        if 'user_id' in request.session:
            user_id = request.session.get('id')
            try:
                sprovider = SPregistration.objects.get(id=user_id)
                sprovider.logout = True
                sprovider.login = False
                sprovider.save()
                messages.success(request, 'logout successful')
                del request.session['user_id']
                return redirect('/mainpg/')
            except SPregistration.DoesNotExist:
                request.session.pop('user_id', None)
                messages.error(request, 'Service provider not found')
        else:
            messages.info(request, 'You are already logged out')
        return redirect('/mainpg/')


def SPhome(request):
    return render(request,"sprovider/index.html")


def viewpost(request):
    viewall = comprequirement.objects.all()
    data = {'data': viewall}
    return render(request, 'sprovider/viewpost.html', context=data)

def SPmessage(request):
    data = comprequirement.objects.all()
    data1 = SPregistration.objects.filter(login=True)
    return render(request, 'sprovider/SPmessage.html', {'data':data,'data1':data1})

def SPaccept(request,id):
    data1 = SPregistration.objects.get(id=id)
    data1.accept = True
    data1.save()
    messages.info(request, 'service provider accepted ')
    return redirect("/SPhome/")

def SPrequest(request,id):
    data= comprequirement.objects.get(id=id)
    data.request = True
    data.save()
    messages.info(request, 'service provider requested ')
    return redirect("/SPhome/")

def SPagreecontract(request):
    data = SPregistration.objects.filter(contract=True,contractapprov=True)
    return render(request, 'sprovider/SPcontract.html', {'data':data})


def SPagree(request,id):
    data = SPregistration.objects.get(id=id)
    data.agree = True
    data.save()
    messages.info(request, 'service provider agreed to contract and viewed negotiation time')
    return redirect("/SPhome/")


def spprovidedata(request):
    data2=SPregistration.objects.get(login=True)
    mail=data2.companyemailid
    data = comprequirement.objects.get(companyemailid=mail)
    return render(request, 'sprovider/spsenddata.html', {'data1': data,'data2': data2})

import random
def spleakeddata(request,id):
    data = SPregistration.objects.get(id=id)
    p = random.randint(1000, 50000)
    data.zkpidentifier= f"zkp-{p}"
    data.leakdata= True
    data.save()
    messages.info(request, 'data leaked done')
    return redirect("/SPhome/")


def spuploaddata(request):
    data1 = SPregistration.objects.get(login=True)
    if request.method == 'POST':
        fileupload = request.FILES.get('fileupload')
        data1.fileupload1 = fileupload
        data1.save()
        messages.success(request, 'data sources uploaded successfully')
        return redirect('/SPhome/')  # Redirect to a success page

    return render(request, 'sprovider/uploadspdata.html',{'data1':data1})


def spsendingdata(request):
    data=SPregistration.objects.filter(login=True)
    return render(request, 'sprovider/spsendingdata.html', {'data': data})

def spgavedata(request,id):
    data = SPregistration.objects.get(id=id, login=True)
    data.sendtooutsoucees=True
    data.save()
    messages.success(request, 'service provider sent data to outsoucees successfully')
    return redirect("/SPhome/")



