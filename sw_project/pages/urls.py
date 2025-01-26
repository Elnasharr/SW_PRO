from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('universities/', views.universities, name='universities'),  
    path('universities/<int:id>/', views.university_details, name='university_details'),  
    path('scholarships/', views.scholarships, name='scholarships'), 
    path('scholarships/<int:id>/', views.scholarship_details, name='scholarship_details'),  
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('compare-universities/', views.compare_universities, name='compare_universities'),
    path('compare-scholarships/', views.compare_scholarships, name='compare_scholarships'),
]