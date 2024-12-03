from django.urls import path
from . import  views



app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('comming-soon/', views.comming_soon, name='comming_soon'),
    path('services/', views.services, name='services'),
    path('service/<str:slug>/', views.service_detail, name='service_detail'),
    path('team-us/', views.team_members, name='team'),
    path('team-us/<str:slug>/', views.team_member_detail, name='team_member'),
    path('projects/', views.projects, name='projects'),
    path('project/<str:slug>/', views.project_detail, name='project_detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('bootcamps/', views.bootcamps, name='boot_camps')
]
