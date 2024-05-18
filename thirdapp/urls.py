from django.urls import path
from . import views
urlpatterns=[
    path('flindex/',views.findex),
    path('',views.findex),
    path('onlineclasses/',views.fonclass),
    path('flogout/',views.flogout),
    path('flnote/',views.fenotes),
    path('fltasks/',views.fetask),





]