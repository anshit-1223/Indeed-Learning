from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('batches/',views.batches),
    path('lectures/',views.lectures),
    path('liveclasses/',views.liveclasses),
    path('logout/',views.logout),
    path('note/',views.note),
    path('softwarekit/',views.softwarekit),
    path('tasks/',views.tasks),
    path('uprofile/',views.uprofile),
    path('lecturesvideo/',views.lecturesvideo),
    path('stask/',views.stask),




]