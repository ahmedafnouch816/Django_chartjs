from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customr/', views.customr, name='customr'),
    path('procurement/', views.procurement, name='procurement'),        
    path('opprtunity/', views.opportunity, name='opportunity'),
    path('rh/', views.rh, name='rh'),
    
]