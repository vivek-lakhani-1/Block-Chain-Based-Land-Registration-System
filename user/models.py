from django.db import models

class Add_property(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    survey_no =  models.IntegerField()
    wallet_address = models.CharField(max_length=256)
    property_id = models.IntegerField()
    document  = models.FileField(upload_to = 'static/uploads/doc_property/')
    Date = models.TextField()
    Total_Owners = models.IntegerField()
    status = models.CharField(max_length=256)

    def __str__(self):
        return self.wallet_address
