from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('about/',views.aboutus),
    path('contact/',views.contact),
    path('feedback/',views.feedback),
    path('login/',views.login),
    path('flogin/',views.flogin),
    path('registration/',views.registration),
    path('placements/',views.placements),
    path('newbatches/',views.mynewbatches),
    path('facility/',views.facility),
]