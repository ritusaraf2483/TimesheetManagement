from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

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
          return super().form_valid(form)

class WorkdayUpdate(LoginRequiredMixin,UpdateView):
     model=Workday
     template_name='workday/workday_update.html'
     form_class=WorkdayForm
     success_url = reverse_lazy("Workday:workday_list")
     login_url = 'Users:login'


class WorkdayDelete(LoginRequiredMixin,DeleteView):
     model = Workday
     fields=['docid']
     template_name = 'workday/workday_delete.html'
     success_url = reverse_lazy("Workday:workday_list")
     login_url = 'Users:login'

