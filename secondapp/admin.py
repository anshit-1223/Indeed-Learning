from django.contrib import admin
from .models import *
# Register your models here.

class mysoftwareAdmin(admin.ModelAdmin):
    list_display=('id','software_title','software_description','software_picture','software_date','software_url')
admin.site.register(mysoftware,mysoftwareAdmin)



