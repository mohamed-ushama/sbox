import random

from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


from outsourcingportal.models import compregistration,comprequirement
from serviceproviders.models import SPregistration
from outsourcees.models import outsourceesregistration
#Szfrom ZKPprotocols.models import zkpregistration

# Create your views here.
def Mlogin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        try:
            if email=="admin@gmail.com" and password=="admin":
                messages.success(request, " manager login successfully")
                return render(request, "manager/home.html")
            elif email == "admin@gmail.com" and password != "admin":
                messages.success(request," manager not login successfully")
                return render(request, "manager/login.html")
            elif email != "admin@gmail.com" and password == "admin":
                messages.success(request," manager not login successfully")
                return render(request, "manager/login.html")
        except:
            messages.success(request, " not login successfully")
            return render(request, "manager/login.html")
    return render(request, "manager/login.html")


def managerpg(request):
    return render(request, "manager/home.html")

def viewoportal(request):
    viewall = compregistration.objects.all()
    data = {'data': viewall}
    return render(request,'manager/outsourcecheck.html',context=data)

def opapprove(request,id):
    data = compregistration.objects.get(id=id)
    data.approve = True
    data.save()
    messages.info(request, " organisation approved successfully.")
    return redirect("/Mhome/")


def opreject(request,id):
    data = compregistration.objects.get(id=id)
    data.reject=True
    data.save()
    messages.info(request, " organisation rejected ")
    return redirect("/Mhome/")



def viewSprovider(request):
    viewall = SPregistration.objects.all()
    data = {'data': viewall}
    return render(request,'manager/Sproviderscheck.html',context=data)

def spapprove(request,id):
    data = SPregistration.objects.get(id=id)
    p = random.randint(100, 500)
    spid = f"SP-{p}"
    data.spid = spid
    data.save()
    data.approve = True
    data.save()
    messages.info(request, " Service providers approved successfully.")
    return redirect("/Mhome/")


def spreject(request,id):
    data = SPregistration.objects.get(id=id)
    data.reject=True
    data.save()
    messages.info(request, " Service providers  rejected ")
    return redirect("/Mhome/")


def viewoutsourcees(request):
    viewall = outsourceesregistration.objects.all()
    data = {'data': viewall}
    return render(request,'manager/outsourceescheck.html',context=data)

def outsourceesapprove(request,id):
    data = outsourceesregistration.objects.get(id=id)
    data.approve = True
    data.save()
    messages.info(request, " outsourcees approved successfully.")
    return redirect("/Mhome/")


def outsourceesreject(request,id):
    data = outsourceesregistration.objects.get(id=id)
    data.reject=True
    data.save()
    messages.info(request, "outsourcees rejected ")
    return redirect("/Mhome/")

def contractdata(request):
    viewall = comprequirement.objects.all()
    viewall1 = SPregistration.objects.all()
    data = {'data': viewall, 'data1': viewall1}
    return render(request, 'manager/contractapprove.html', context=data)

def contractapprove(request,id):
    data = SPregistration.objects.get(id=id)
    data.contractapprov=True
    data.save()
    messages.info(request, "manager approved contract successfully")
    return redirect("/Mhome/")
def contractreject(request,id):
    data = SPregistration.objects.get(id=id)
    data.contractreject=True
    data.save()
    messages.info(request,"manager rejected contract successfully")
    return redirect("/Mhome/")

def complaintdata(request):
    data = SPregistration.objects.filter(sendtooutsoucees=True)
    return render(request, 'manager/outscomplaint.html', {'data': data})

def complaintinspect(request,id):
    data = SPregistration.objects.get(id=id)

    if data.industry == "Technology":
        data.solution = "Report to the data privacy regulator(GDPR)if tracking is deemed excessive or intrusive. immediate cessation of unauthorized data sharing."
    if data.industry == "Finance":
        data.solution = "Report to suspicious activity to the financial regulatory(GLBA).legal action against both parties for negligence and potential financial losses."
    if data.industry == "Manufacturing":
        data.solution = "Report to(GDPR),Contact regulatory agencies and affected customers, informing them of the leak and potential product safety concerns. "
    if data.industry == "Healthcare":
        data.solution = "Report the leak to the data privacy regulator(HIPAA) and consider legal action for potential harm to patient privacy and disruption of healthcare services."
    if data.industry == "Retail":
        data.solution = "Unsubscribe from unwanted marketing and report any suspicious activity to the data privacy regulator(CCPA/CPRA),security for affected account "
    if data.industry == "Legal Services":
        data.solution = "Report the leak to the bar association and consider legal action against LegalEase for professional negligence and breach of client confidentiality"
    if data.industry == "Education":
        data.solution = "Report the leak to administration and data privacy authorities for Department of Education data security protocols for student information systems"
    if data.industry == "Media & Entertainment":
        data.solution = "update data security protocols,Report the leak to relevant authorities and consider legal action for unfair trade practices and copyright infringement"
    data.inspect=True
    data.save()
    messages.info(request, 'inspection done successfully')
    return redirect("/Mhome/")


def sendingsolution(request):
    data = SPregistration.objects.filter(sendtooutsoucees=True)
    return render(request, 'manager/sendsolution.html', {'data': data})


def sentsolution(request,id):
    data = SPregistration.objects.get(id=id)
    data.sendsolution=True
    data.save()
    messages.info(request,"Manager Sent solution successfully")
    return redirect("/Mhome/")