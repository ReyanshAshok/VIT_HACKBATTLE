from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class TestModel(models.Model):
    test = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
    def published_recenlty(self):
        return self.pub_date>=timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.test


class ScoutingRegistration(models.Model):
    name_of_organization= models.CharField(max_length=200)
    name_of_person = models.CharField(max_length=200)
    region=models.CharField(max_length=200)
    contact_number=models.IntegerField(max_length=20000)
    num_of_pos_available=models.IntegerField(default=100)
    email=models.EmailField(max_length=200)
    qualification = models.CharField(max_length=200)
    area_of_interest= models.CharField(max_length=2000)


class TeachingRegistration(models.Model):
    # name_of_organization = models.CharField(max_length=200)
    name_of_person = models.CharField(max_length=200,null=True)
    region = models.CharField(max_length=200,null=True)
    contact_number = models.IntegerField(null=True)
    # num_of_pos_available = models.IntegerField(default=100)
    email = models.EmailField(max_length=200,null=True)
    subject_taught = models.TextField(max_length=200,null=True)
    qualification = models.CharField(max_length=200,null=True)
    # area_of_interest = models.CharField(max_length=2000)


class VolenteerRegistration(models.Model):
    name= models.CharField(max_length=200)
    region=models.CharField(max_length=200)
    contact_number=models.IntegerField(max_length=20000)
    email=models.EmailField(max_length=200)
    area_of_interest= models.CharField(max_length=2000)



class Choice(models.Model):
    cool= models.ForeignKey(TestModel,on_delete=models.CASCADE)
    choice_text= models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

