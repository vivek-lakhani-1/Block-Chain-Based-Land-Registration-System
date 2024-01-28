from django.shortcuts import render,redirect
from .models import Register_Data
from rest_framework.decorators import api_view
import threading
from decouple import config
from .custom_modules import *
from geopy.geocoders import Nominatim
from rest_framework import response,status
import random

@api_view(['GET'])
def Validate_email_Link(request,cipher_text):
    try:
        decrypted_text = cipher_suite.decrypt(cipher_text)
        email = decrypted_text.decode('utf-8')
        query = Register_Data.objects.get(Email_Id=email)
        if(query != None):
            query.is_verified = True
            query.save()
            prm = {
                    'title' : 'Verified',
                    'message' : "Your Email Address is Verified"
                }
            return render(request,'verified.html',prm)
    except:
        # return response.Response({'status':404,'message':'Page Not Found !!'},status=status.HTTP_404_NOT_FOUND)
        return render(request,'404.html')

def Register(request,param=None):
    if(request.method == "POST" ):
            try:
                query = Register_Data.objects.filter(Email_Id = request.POST.get('Email_Id'))
                if(query.exists()):
                    param = {
                        'errormsg':True
                    }
                    param['message'] = 'Duplicate Entry Not Allowed'
                    
                    return render(request,'register.html',param)
                    
                else:
                    # Reg = Register_Data()
                    # Reg.Email_Id = request.POST.get('Email_Id')
                    # Reg.Password = request.POST.get('Password')
                    # Reg.Phone_Number = request.POST.get('Phone_Number')
                    # Reg.Name = request.POST.get('Name')
                    # Reg.Wallet_address = request.session.get('wallet', None)
                    # Reg.Address = request.POST.get('Address')
                    # Reg.City =  request.POST.get('City')
                    # Reg.Aadhar_card_doc =  request.FILES['Aadhar']
                    # Reg.Pan_card_doc = request.FILES['Pan']
                    # Reg.Profile_Photo = request.FILES['Profile']
                    # Reg.Email_Verified= False
                    # Reg.save()
                    # my_thread = threading.Thread(target=Validate_Email, args=(request.POST.get('Email_Id'),))
                    # my_thread.start()
                    return redirect('/user/dashboard')
            except:
                return redirect(request,'Error.html')
    return render(request,'register.html')


def homepage(request):
    return render(request,'homepage.html')    

def login_API_Web(request):
    if(request.method == "POST"):
            Email_id = request.POST.get('Email_Id')
            Password =  request.POST.get('Password')
    
            try:
                query = Register_Data.objects.filter(Email_Id = Email_id)
                if(query.exists()):
                   query = query.values()[0]
                   if(query['Password'] == Password):
                       return redirect('/user/dashboard')
                   else:
                       return redirect('/login')
                    
                else:
                    return redirect('/register')
            except:
                return redirect(request,'Error.html')
    return redirect('/login')


@api_view(['GET'])
def wallet_data(request):
    data = str(request.GET.get('data')).split("|||")
    request.session['wallet'] = data[0]
    query = Register_Data.objects.filter(Wallet_address = data[0])
    if(query.exists()):
        query = query.values()[0]
        if(query['Email_Id'] == ""):
            return response.Response({'status':200,'message':'Working'},status=status.HTTP_200_OK)
        else:
            return response.Response({'status':200,'message':'Already'},status=status.HTTP_200_OK)
    else:
        return response.Response({'status':200,'message':'Working'},status=status.HTTP_200_OK)
    

def user_profile(request):
    return render(request,'user_profile.html')