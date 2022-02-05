from django.urls import re_path
from .import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),

    #comon page a s j

    re_path(r'^Applyleave$', views.Applyleave, name='Applyleave'),
   
    #Jishnu

    re_path(r'^applyleavesub$', views.applyleavesub, name='applyleavesub'),

    #Seban

    re_path(r'^Requestedleave$', views.Requestedleave, name='Requestedleave'),
    
    #Althaf
    
    re_path(r'^trainers_leave$', views.trainers_leave, name='trainers_leave'),
    re_path(r'^trainees_leave$', views.trainees_leave, name='trainees_leave'),
]