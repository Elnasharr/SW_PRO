from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('universities/', views.universities, name='universities'),  
    path('universities/<int:university_id>/', views.university_details, name='university_details'),  
    path('scholarships/', views.scholarships, name='scholarships'), 
    path('scholarships/<int:scholarship_id>/', views.scholarship_details, name='scholarship_details'),  
   
]
#last
