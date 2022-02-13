import datetime

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from usermanagement.models import Profile
from workdaymanagement.forms import WorkdayForm
from workdaymanagement.models import Workday


def home(request):
     return render(request,'home.html')

class GetList(ListView):
     model=Workday
     template_name = 'workday/workday_list.html'

class UserDetail(DetailView):
     model=Workday
     template_name = 'workday/workday_detail.html'


class WorkdayCreate(LoginRequiredMixin,CreateView):
     model=Workday
     form_class = WorkdayForm
     template_name = 'workday/workday_new.html'
     success_url = reverse_lazy("Workday:workday_list")
     login_url= 'Users:login'

     def form_valid(self, form):
          form.instance.docid = self.request.user.id
          form.instance.doctor = self.request.user.username
          time1 = datetime.datetime.strptime(str(form.instance.time_in),"%H:%M:%S")
          time2 = datetime.datetime.strptime(str(form.instance.time_out),"%H:%M:%S")
          difference = time2 - time1
          form.instance.hours_worked=difference
          totalpayroll=(difference.seconds)*(form.instance.payroll/3600)
          form.instance.total_payroll=totalpayroll
          return super().form_valid(form)

class WorkdayUpdate(LoginRequiredMixin,UpdateView):
     model=Workday
     template_name='workday/workday_update.html'
     #form_class=WorkdayForm
     fields = '__all__'
     success_url = reverse_lazy("Workday:workday_list")
     login_url = 'Users:login'

     def get_object(self,queryset=None):
           obj = UpdateView.get_object(self,queryset=None)
           if obj.docid == self.request.user.id:
                return obj
           else:
                raise ValidationError('You are not an authorized user')

class WorkdayDelete(LoginRequiredMixin,DeleteView):
     model = Workday
     fields=['docid']
     template_name = 'workday/workday_delete.html'
     success_url = reverse_lazy("Workday:workday_list")
     login_url = 'Users:login'

     def get_object(self,queryset=None):
           obj = UpdateView.get_object(self,queryset=None)
           if obj.docid == self.request.user.id:
                return obj
           else:
                raise ValidationError('You are not an authorized user')

def GenerateReport(request):
     if request.method=="POST":
          startdate=request.POST.get('start_date')
          enddate = request.POST.get('end_date')
          reportdata = Workday.objects.filter(work_date__gte=startdate).filter(work_date__lte=enddate)

          error_message = None
          if not startdate:
               error_message = "Start date required"
          elif not enddate:
               error_message = "End date required"

          if not error_message:
               return render(request, 'home.html', {'reportdata': reportdata})
          else:
               context = {'error_message': error_message}
               return render(request,'home.html', context)
     else:
          return render(request, 'home.html')