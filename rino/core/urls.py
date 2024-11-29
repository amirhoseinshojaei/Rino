from django.urls import path
from . import  views



app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('comming-soon/', views.comming_soon, name='comming_soon'),
    path('services/', views.services, name='services'),
    path('service/<str:slug>/', views.service_detail, name='service'),
    path('team-us/', views.team_members, name='team'),
]