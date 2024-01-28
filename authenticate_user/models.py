from django.db import models

# class Register_Data(models.Model):
#     # wallet_address = models.CharField(max_length=256)
#     Email_Id = models.EmailField()
#     Name = models.CharField(max_length=256)
#     Age = models.IntegerField()
#     Phone_Number = models. IntegerField()
#     Address = models.CharField(max_length=256)
#     City = models.CharField(max_length=256)
#     Aadhar_card_doc = models.FileField(upload_to='static/uploads/user_aadhar/')
#     Pan_card_doc = models.FileField(upload_to='static/uploads/user_pan/')
#     Profile_Photo = models.FileField(upload_to='static/uploads/user_profile/')
    

class Register_Data(models.Model):
    Wallet_address = models.CharField(max_length=256)
    Email_Id = models.EmailField()
    Name = models.CharField(max_length=256)
    Age = models.IntegerField()
    Password = models.CharField(max_length = 256)
    Phone_Number = models.IntegerField()
    Address = models.CharField(max_length=256)
    City = models.CharField(max_length=256)
    Aadhar_card_doc = models.FileField(upload_to='static/uploads/user_aadhar/')
    Pan_card_doc = models.FileField(upload_to='static/uploads/user_pan/')
    Profile_Photo = models.FileField(upload_to='static/uploads/user_profile/')
    Email_Verified =  models.BooleanField(default=True)