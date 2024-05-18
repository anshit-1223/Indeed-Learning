from django.contrib import admin
from .models import *

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','msg')
admin.site.register(contactus,contactusAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display=('id','headlines','slider_description','slider_picture')
admin.site.register(slider,sliderAdmin)

class newbatchesAdmin(admin.ModelAdmin):
    list_display=('id','bname','bpic','bdate')
admin.site.register(newbatches,newbatchesAdmin)

class collegeAdmin(admin.ModelAdmin):
    list_display=('id','college_name')
admin.site.register(college,collegeAdmin)

class session_yearAdmin(admin.ModelAdmin):
    list_display=('id','session')
admin.site.register(session_year,session_yearAdmin)

class batchAdmin(admin.ModelAdmin):
    list_display=('id','batch_name')
admin.site.register(batch,batchAdmin)

class placementAdmin(admin.ModelAdmin):
    list_display=('id','student_picture','student_name','college','session','batch','company_name','company_logo')
admin.site.register(placement,placementAdmin)

class signupAdmin(admin.ModelAdmin):
    list_display=('name','email','passwd','mobile','profile','course','pyear','college','batch','status','batchid')
admin.site.register(signup,signupAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name','category_picture','category_date')
admin.site.register(category,categoryAdmin)

class studentbatchAdmin(admin.ModelAdmin):
    list_display=('id','batch_name')
admin.site.register(studentbatch,studentbatchAdmin)

class mylecturesAdmin(admin.ModelAdmin):
    list_display=('id','video_category','video_batch','vlink','thumbnail','video_description','added_date')
admin.site.register(mylectures,mylecturesAdmin)

class batchtimingAdmin(admin.ModelAdmin):
    list_display=('id','clname','batch','clink','timing','start_date')
admin.site.register(batchtiming,batchtimingAdmin)

class enotesAdmin(admin.ModelAdmin):
    list_display=('id','title','notes_pic','pdf_notes','added_date','batch')
admin.site.register(enotes,enotesAdmin)

class instructorAdmin(admin.ModelAdmin):
    list_display=('id','instructor_name','qualif','instructor_post','instructor_pic')
admin.site.register(instructor,instructorAdmin)

class mytaskAdmin(admin.ModelAdmin):
    list_display=('id','taskbatch','title','task_file','added_date')
admin.site.register(mytask,mytaskAdmin)

class submittedtaskAdmin(admin.ModelAdmin):
    list_display=('id','title','answer_file','tid','userid','marks')
admin.site.register(submittedtask,submittedtaskAdmin)

class fsignupAdmin(admin.ModelAdmin):
    list_display=('fid','name','email','mobile','passwd')
admin.site.register(fsignup,fsignupAdmin)