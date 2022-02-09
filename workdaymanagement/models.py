from datetime import date

from django.db import models
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
     user=models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True)
     location=models.ForeignKey(Location,on_delete=models.CASCADE,blank=True)
     sector=models.CharField(max_length=7,blank=True)
     work_date=models.DateField(default=date.today,blank=True)
     time_in=models.TimeField()
     time_out=models.TimeField()
     hours_code=models.ForeignKey(Payroll,on_delete=models.CASCADE)
     payroll=models.FloatField()

     def get_absolute_url(self):
          return reverse('Workday:workday_list')