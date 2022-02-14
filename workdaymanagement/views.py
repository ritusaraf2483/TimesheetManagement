import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from workdaymanagement.forms import WorkdayForm
from workdaymanagement.models import Workday


def home(request):
     return render(request,'home.html')

class RedirectToPreviousMixin:

    default_redirect = '/'

    def get(self, request, *args, **kwargs):
        request.session['previous_page'] = request.META.get('HTTP_REFERER', self.default_redirect)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session['previous_page']

class GetList(ListView):
     model=Workday
     template_name = 'workday/workday_list.html'

class UserDetail(DetailView):
     model=Workday
     template_name = 'workday/workday_detail.html'


class WorkdayCreate(RedirectToPreviousMixin,LoginRequiredMixin,CreateView):
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

     def get_object(self,queryset=None):
           obj = CreateView.get_object(self,queryset=None)
           obj1=DetailView.get_object(self,queryset=None)
           if obj1.docid == self.request.user.id:
                return obj
           else:
                raise ValidationError('You are not an authorized user')

class WorkdayUpdate(RedirectToPreviousMixin,LoginRequiredMixin,SuccessMessageMixin,UpdateView):
     model=Workday
     template_name='workday/workday_update.html'
     form_class=WorkdayForm
     #success_url = reverse_lazy("Workday:workday_list")
     login_url = 'Users:login'
     success_message = "Workday has been updated"

     def get_object(self,queryset=None):
           obj = UpdateView.get_object(self,queryset=None)
           if obj.docid == self.request.user.id:
                return obj
           else:
                raise ValidationError('You are not an authorized user')

class WorkdayDelete(RedirectToPreviousMixin,LoginRequiredMixin,DeleteView):
     model = Workday
     fields=['docid']
     template_name = 'workday/workday_delete.html'
     #success_url = reverse_lazy("Workday:workday_list")
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
          doctorid=request.POST.get('Doctor_id')
          if (startdate and enddate):
               reportdata = Workday.objects.filter(work_date__gte=startdate).filter(work_date__lte=enddate)
               return render(request, 'home.html', {'reportdata': reportdata})
          elif (doctorid):
               reportdata = Workday.objects.filter(docid=doctorid)
               return render(request, 'home.html', {'reportdata': reportdata})
          elif (doctorid and startdate and enddate):
               #reportdata=Workday.objects.filter(work_date__gte=startdate).filter(work_date__lte=enddate).filter(docid=doctorid)
               reportdata = Workday.objects.filter(docid=3)
               #reportdata = q1.objects.filter(work_date__gte=startdate,work_date__lte=enddate)
               return render(request, 'home.html', {'reportdata': reportdata})

          error_message = None
          if (enddate and not startdate):
               error_message = "Start date required"
          elif (startdate and not enddate):
               error_message = "End date required"
          elif not(enddate and startdate and doctorid):
               error_message = "Data required"

          if error_message:
               context = {'error_message': error_message}
               return render(request,'home.html', context)
     else:
          return render(request, 'home.html')