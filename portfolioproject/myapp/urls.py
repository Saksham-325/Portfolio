
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name="home"),
    path('about/',views.about,name='about'),
    path('contacts/',views.contacts,name='contacts'),
    path('educations/',views.educations,name='educations'),
    path('skills/',views.skills,name='skills'),
    path('projects/',views.projects,name='projects'),
    
]