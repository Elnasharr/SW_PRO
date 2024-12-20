from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('universities/', views.universities, name = 'universities'),
    path('scholarships/', views.scholarships, name = 'scholarships'),
    path('universities/university_details/<int:id>', views.university_details, name = 'university_details'),
    path('scholarships/scholarship_details/<int:id>', views.scholarship_details, name = 'scholarship_details'),
]