from django.db import models
# class customerData(models.Model):
#     username = models.CharField(primary_key=True,max_length=100)
#     password = models.CharField(max_length=100)
#     mobile = models.IntegerField(unique=True)
    
class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.IntegerField(unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    age = models.IntegerField()
    
    def __str__(self):
        return self.username
