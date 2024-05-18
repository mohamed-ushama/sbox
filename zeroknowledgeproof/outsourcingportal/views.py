from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from serviceproviders.models import SPregistration
from outsourcees.models import outsourceesregistration
# Create your views here.
def mainpage(request):
    return render(request,"mainpage/home.html")

def OPregister(request):
    if request.method=="POST":
        companyname=request.POST['companyname']
        companyemailid=request.POST['companyemailid']
        contactperson=request.POST['contactperson']
        phoneno=request.POST['phoneno']
        country = request.POST['country']
        password=request.POST['password']
        try:
            compregistration(companyname=companyname,companyemailid=companyemailid,contactperson=contactperson,phoneno=phoneno,country=country,password=password).save()
            messages.success(request, " Organisation registered successfully")
            return render(request,"Oportal/login.html")
        except:
            messages.info(request," Organisation not registered successfully")
            return render(request, "Oportal/register.html")

    return render(request,"Oportal/register.html")


def OPlogin(request):
    if request.method == 'POST':
        companyemailid = request.POST.get('companyemailid')
        password = request.POST.get('password')

        try:
            oportal = compregistration.objects.get(companyemailid=companyemailid, password=password)

            if oportal.approve:
                messages.info(request, "organization Login Successful")
                request.session['user_id'] =oportal.id
                print(request.session['user_id'])
                oportal.login = True
                oportal.logout = False
                oportal.save()

                return redirect("/ophome/")
            else:
                messages.info(request, "organization need management approval to access")
                return render(request,"Oportal/login.html")

        except compregistration.DoesNotExist:
            messages.info(request, " organization enter Invalid Email or Password")

    return render(request,"Oportal/login.html")

def OPlogout(request):
        if 'user_id' in request.session:
            user_id = request.session.get('id')
            try:
                client = compregistration.objects.get(id=user_id)
                client.logout = True
                client.login = False
                client.save()
                del request.session['user_id']
                return redirect('/mainpg/')
            except compregistration.DoesNotExist:
                request.session.pop('user_id', None)
                messages.error(request, 'organization not found')
        else:
            messages.info(request, 'You are already logged out')

        return redirect('/mainpg/')

def oportalhome(request):
    return render(request,"Oportal/ophome.html")

def oportalrequirement(request):
    try:
        data = compregistration.objects.get(login=True)
        companyname = data.companyname
        contactperson = data.contactperson
        companyemailid=data.companyemailid
    except compregistration.DoesNotExist:
        pass
    if request.method == "POST":
        location = request.POST.get('location')
        industry = request.POST.get('industry')
        serviceneed = request.POST.get('serviceneed')
        duration = request.POST.get('duration')
        budget = request.POST.get('budget')
        instance = comprequirement(
            companyname=companyname,
            contactperson=contactperson,
            companyemailid=companyemailid,
            location=location,
            industry=industry,
            serviceneed=serviceneed,
            duration=duration,
            budget=budget,

        )
        instance.save()
        data = compregistration.objects.get(login=True)
        data.upload = True
        data.save()
        messages.info(request, " organisation Uploaded requirement successfully")
        return redirect("/ophome/")
    return render(request, "Oportal/requirement.html", {'companyname': companyname, 'contactperson': contactperson})


def SPdata(request):
    viewall = SPregistration.objects.filter(accept=True)
    data = {'data': viewall}
    return render(request, 'Oportal/viewSPdata.html', context=data)

def contract(request):
    viewall = SPregistration.objects.filter(accept=True)
    data = {'data': viewall}
    return render(request, 'Oportal/addprotocol.html', context=data)

def addcontract(request,spid):
    sp= SPregistration.objects.get(spid=spid)
    data1= comprequirement.objects.get()
    companyemailid=data1.companyemailid
    budget=data1.budget
    duration = data1.duration
    serviceneed=data1.serviceneed
    industry=data1.industry

    sp.companyemailid= data1.companyemailid
    sp.budget = data1.budget
    sp.duration = data1.duration
    sp.serviceneeded = data1.serviceneed

    if duration=="3 Month":
        sp.contractlength="1 year"
    elif duration=="6 Month":
        sp.contractlength="2 year"
    elif duration=="9 Month":
        sp.contractlength="3 year"
    elif duration=="More than a year":
        sp.contractlength="4 year"

    if budget=="1-3 Laks":
         sp.Ntime="4 weeks"
    elif budget=="4-6 Laks":
        sp.Ntime="8 weeks"
    elif budget=="7-10 Laks":
        sp.Ntime="12 weeks"

    if industry=="Technology":
        sp.SLA="99% uptime, 24/7 support"
        sp.DataSecurity="AES 256 encryption, regular audits"
        sp.IPownership="Shared ownership with contributions defined"
        sp.DisputeResolution="Arbitration"
        sp.TerminationClauses="Material breach, insolvency"
        sp.NegotiationPoints="Technical expertise, pricing, service guarantees"
        sp.DesiredOutcomes="Competitive rates, transparent pricing, long-term partnership"
        sp.ClauseRational="Secure data handling, IP protection"


    elif industry=="Finance":
        sp.SLA = "99.5% accuracy, real-time processing"
        sp.DataSecurity ="compliance,data encryption"
        sp.IPownership ="Shared ownership with contributions defined"
        sp.DisputeResolution ="Litigation"
        sp.TerminationClauses ="Material breach, bankruptcy"
        sp.NegotiationPoints ="Regulatory compliance, technology innovation"
        sp.DesiredOutcomes ="Efficient verification process, cost reduction"
        sp.ClauseRational ="Secure management, data privacy"

    elif industry=="Manufacturing":
        sp.SLA = "98% product traceability, real-time quality monitoring"
        sp.DataSecurity ="Zero-trust security architecture, data provenance tracking"
        sp.IPownership ="Client retains ownership"
        sp.DisputeResolution ="Binding arbitration"
        sp.TerminationClauses ="Failure to meet SLAs, data breaches"
        sp.NegotiationPoints ="Industry experience, ZKP integration expertise"
        sp.DesiredOutcomes ="Enhanced worktransparency, improved quality control"
        sp.ClauseRational ="Secure management, data privacy"


    elif industry=="Healthcare":
        sp.SLA = "99.9% data availability, HIPAA compliance"
        sp.DataSecurity ="Blockchain-based data storage, encryption at rest and in transit"
        sp.IPownership ="Client retains ownership"
        sp.DisputeResolution ="Binding arbitration"
        sp.TerminationClauses ="Misuse of patient data, security breaches"
        sp.NegotiationPoints ="Scalability, compliance expertise, privacy-preserving solutions"
        sp.DesiredOutcomes ="Streamlined claims processing, reduced costs"
        sp.ClauseRational ="Data security, patient privacy guaranteed"



    elif industry=="Legal Services":
        sp.SLA = "95% accuracy, 3-day response time"
        sp.DataSecurity ="Multi-factor authentication, access controls"
        sp.IPownership ="Client retains ownership"
        sp.DisputeResolution ="Mediation"
        sp.TerminationClauses ="Failure to meet SLAs, non-payment"
        sp.NegotiationPoints ="ZKP expertise, legal domain knowledge"
        sp.DesiredOutcomes ="Improved legal research efficiency, data privacy"
        sp.ClauseRational ="Cost-effective, flexible service model"


    elif industry == "Retail":
        sp.SLA = "99.9% order accuracy, real-time inventory updates"
        sp.DataSecurity ="Secure order processing platform, encrypted inventory data"
        sp.IPownership ="Client retains ownership"
        sp.DisputeResolution ="Mediation"
        sp.TerminationClauses ="Failure to meet SLAs, data breaches"
        sp.NegotiationPoints ="Industry expertise, inventory management solutions"
        sp.DesiredOutcomes ="Improved order processing efficiency, reduced costs"
        sp.ClauseRational ="Secure order processing, inventory data privacy"


    elif industry == "Media & Entertainment":
        sp.SLA = "99.9% content availability, copyright protection"
        sp.DataSecurity ="Content encryption, secure access controls"
        sp.IPownership ="Client retains ownership"
        sp.DisputeResolution ="Litigation"
        sp.TerminationClauses ="Content piracy, data breaches"
        sp.NegotiationPoints ="Technology expertise, content management solutions"
        sp.DesiredOutcomes ="Secure content management, copyright protection"
        sp.ClauseRational ="Scalability, cost-effective solution"


    elif industry == "Education":
        sp.SLA = "99.99% exam integrity, student privacy protection"
        sp.DataSecurity ="Secure testing environment, encryption of student data"
        sp.IPownership ="Client retains ownership"
        sp.DisputeResolution ="Mediation"
        sp.TerminationClauses ="Failure to ensure exam integrity, data leaks"
        sp.NegotiationPoints ="ZKP expertise, educational technology experience"
        sp.DesiredOutcomes ="Secure online exam proctoring, student data privacy"
        sp.ClauseRational ="Data security, student privacy guaranteed"

    sp.contract=True
    sp.save()
    messages.info(request, 'Contract added successfully')
    return redirect("/ophome/")

def negotime(request):
    viewall= SPregistration.objects.filter(accept=True)
    viewall1 = outsourceesregistration.objects.all()
    return render(request, 'Oportal/negotime.html',  {'data1': viewall,'data2': viewall1})

def sendnegotime(request, id):
        sp = SPregistration.objects.get(id=id)# value
        sp.sendntimeoutsourcees = True
        sp.save()
        messages.info(request, 'Negotiation Time sent to Outsourcees successfully')
        return redirect("/ophome/")

def download(request):
    return render(request,'a.html')





######################################################################

import os
def uploaddataset(request):

    data = compregistration.objects.get(login=True)
    email=data.companyemailid
    data11 = comprequirement.objects.get(companyemailid=email)
    if request.method == 'POST':
        fileupload1 = request.FILES.get('fileupload1')
        data11.fileupload1 = fileupload1
       # data11.key = encryption_key
        data11.save()
        file_path = data11.fileupload1.path


#####################################################################################################################################################################################
        #ushama     # Save the uploaded file
     #   encryption_key = os.urandom(32)
      #  print(encryption_key)

       #data11.fileupload1 = fileupload1
       #data11.key = encryption_key
       #data11.save()
       #file_path = data11.fileupload1.path

        # Encrypt the uploaded file

       # encrypted_file_path = encrypt_file(file_path, encryption_key)
        #file_name = os.path.basename(encrypted_file_path)
        # Update the database with the encrypted file path
        #data11.fileupload1.name= file_name  # Update the file name, not the path
        #data11.save()

    # Update the database with the encrypted file path

       # data11.fileupload1 = file_name
       # data11.fileupload1.name= file_name
    ##########################################################################################################################################################################################################################################################################
        data11.save()
        data11.save()
        messages.info(request, 'Datasource uploaded successfully')
        return redirect("/ophome/")

    return render(request, 'Oportal/uploaddataset.html', {'data1': data11})


from Crypto.Cipher import AES
import os

def encrypt_file(file_path, key):
        # Generate a random initialization vector (IV) of AES block size (16 bytes)
        iv = os.urandom(AES.block_size)
        # Create AES cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # File names for encrypted output
        encrypted_file_path = file_path + ".encrypted"

        # Open the input file for reading in binary mode
        with open(file_path, 'rb') as infile:
            # Read the entire file content
            file_data = infile.read()

            # Check if the file size is a multiple of the block size (necessary for AES)
            # If not, pad the data to make it a multiple of the block size
            padding_length = AES.block_size - len(file_data) % AES.block_size
            file_data += bytes([padding_length]) * padding_length

            # Encrypt the file data
            encrypted_data = cipher.encrypt(file_data)

            # Write the IV to the beginning of the output file
            with open(encrypted_file_path, 'wb') as outfile:
                outfile.write(iv)
                outfile.write(encrypted_data)

        return encrypted_file_path

#######################################################################################

# def decrypt_file(encrypted_file_path, encryption_key):
#     # Read the initialization vector (IV) and encrypted data from the encrypted file
#     with open(encrypted_file_path, 'rb') as infile:
#         iv = infile.read(AES.block_size)
#         encrypted_data = infile.read()
#
#     # Create AES cipher object with the provided IV and key
#     cipher = AES.new(encryption_key, AES.MODE_CBC, iv)
#
#     # Decrypt the encrypted data
#     decrypted_data = cipher.decrypt(encrypted_data)
#
#     # Remove padding from the decrypted data
#     padding_length = decrypted_data[-1]
#     decrypted_data = decrypted_data[:-padding_length]
#
#     return decrypted_data
#
# # Replace these variables with your encrypted file and encryption key
# encrypted_file_path = r''
# decryption_key = encryption_key  # Use the correct encryption key used for encryption
#
# # Decrypt the file
# decrypted_data = decrypt_file(encrypted_file_path, decryption_key)
#
# #Save the decrypted data to a new file or process it as needed
# output_file_path = r''
# with open(output_file_path, 'wb') as outfile:
#     outfile.write(decrypted_data)




# print(f"File decrypted and saved: {output_file_path}")
# def encryptfile(spencryptfile):
#     viewall = comprequirement.objects.all()
#     for resource in viewall:
#         resource.fileupload1 = spencryptfile
#         resource.save()
# spencryptfile=r'D:\project(ZKP)\zeroknowledgeproof\media\documents\patient_dataset.csv.encrypted'
# encryptfile(spencryptfile)

def senddataset(request):
    data = compregistration.objects.get(login=True)
    email=data.companyemailid
    data = SPregistration.objects.get(companyemailid=email)
    return render(request, 'Oportal/senddataset.html',  {'data2':data})

import random
def sentdata(request,spid):
    data = SPregistration.objects.get(spid=spid)
    p = random.randint(1000, 50000)
    data.zkpidentifier = f"ZKP-{p}"
    data.save()
    messages.info(request, "Data sent to serviceprovider Successfully.")
    return redirect("/ophome/")

