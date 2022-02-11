import datetime

from django import forms
from django.forms import Textarea
from workdaymanagement.models import Workday
SECTOR_CHOICES=(('east','East'),('west','West'),)

class WorkdayForm(forms.ModelForm):
    time_in = forms.TimeField(help_text='Must be in the hour format')
    time_out = forms.TimeField(help_text='Must be in the hour format')
    sector = forms.ChoiceField(choices=SECTOR_CHOICES)

    class Meta:
        model=Workday
        exclude=['docid','doctor']
    def clean(self):
        super(WorkdayForm,self).clean()
        payroll=self.cleaned_data.get('payroll')
        if payroll<=0:
            self._errors['payroll'] = self.error_class([
                'payroll must be positive integer'])
