from django.contrib import admin

from usermanagement.models import Profile


class AdminUser(admin.ModelAdmin):
    list_display = ['phone','address','image']

admin.site.register(Profile,AdminUser)
