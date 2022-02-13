from datetime import date

from django import forms
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from usermanagement.models import Profile


class Location(models.Model):
    location=models.CharField(max_length=20)

    def __str__(self):
         return self.location

class Payroll(models.Model):
     name=models.CharField(max_length=10)

     def __str__(self):
          return self.name

class Workday(models.Model):
     id=models.AutoField(primary_key=True)
     docid=models.IntegerField()
     doctor=models.CharField(max_length=20)
     location=models.ForeignKey(Location,on_delete=models.CASCADE,blank=True)
     sector=models.CharField(max_length=7,blank=True)
     work_date=models.DateField(default=date.today,blank=True)
     time_in=models.TimeField()
     time_out=models.TimeField()
     hours_worked=models.DurationField(blank=True,null=True)
     hours_code=models.ForeignKey(Payroll,on_delete=models.CASCADE)
     payroll=models.DecimalField(max_digits=5, decimal_places=2)
     total_payroll=models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)

     def get_absolute_url(self):
          return reverse('Workday:workday_list')