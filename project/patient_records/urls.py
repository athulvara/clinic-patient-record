from django.urls import path
from . import views

app_name = 'patient_records'

urlpatterns = [
    path('', views.loginn, name='loginn'),
    path('logout', views.logoutt, name='logoutt'),
    path('register/', views.create_patient, name='create_patient'),
    path('list/', views.patient_list, name='patient_list'),


]