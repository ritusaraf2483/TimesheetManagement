from django import forms
from workdaymanagement.models import Workday

class WorkdayForm(forms.ModelForm):
    class Meta:
        model=Workday
        fields='__all__'