from django.contrib import admin
from workdaymanagement.models import Workday, Location, Payroll


class AdminWorkday(admin.ModelAdmin):
    list_display = ['user','location','sector','work_date','time_in','time_out','hours_code','payroll']

class AdminLocation(admin.ModelAdmin):
    list_display = ['location']

class AdminPayroll(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Workday,AdminWorkday)
admin.site.register(Location,AdminLocation)
admin.site.register(Payroll,AdminPayroll)