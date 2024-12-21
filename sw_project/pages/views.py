from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import University, Scholarship, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password
import random
from django.core.mail import send_mail
import time 

# Create your views here.
@login_required
def index(request):
    universities = University.objects.all()[:3]
    all_universities = University.objects.all()
    scholarships = Scholarship.objects.all()[:3]
    context = {
        'universities':universities,
        "all_universities":all_universities,
        'scholarships':scholarships,
    }
    return render(request, 'index.html', context)

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, userID=user_id)  # Fetch the user by ID
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)

@login_required
def scholarship_details(request, id):
       
    scholarship = get_object_or_404(Scholarship, id=id)
    context = {
        'scholarship': scholarship,
    }
    return render(request, 'scholarship-details.html', context)


@login_required
def scholarships(request):
    query = request.GET.get('query', '')
    if query:
        scholarships = Scholarship.objects.filter(
            name__icontains=query
        ) | Scholarship.objects.filter(
            short_description__icontains=query
        ) | Scholarship.objects.filter(
            about__icontains=query
        )
    else:
        scholarships = Scholarship.objects.all()

    context = {
        'scholarships': scholarships,
    }
    return render(request, 'scholarships.html', context)

@login_required
def universities(request):
    query = request.GET.get('query', '')
    if query:
        universities = University.objects.filter(
            name__icontains=query
        ) | University.objects.filter(
            location__icontains=query
        ) | University.objects.filter(
            about__icontains=query
        )
    else:
        universities = University.objects.all()

    context = {
        'universities': universities,
    }
    return render(request, 'universities.html', context)

@login_required
def university_details(request, id):
    university = get_object_or_404(University, id=id)
    context = {
        'university': university,
    }
    return render(request, 'university-details.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)  
            next_url = request.GET.get('next')  # Get the next parameter
            if next_url:  # If next_url is provided, redirect to it
                return redirect(next_url)
            return redirect('index')  # Default redirect if no next parameter
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'login.html')


otp_storage = {}

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'An account with the same email exists.')
        else:
            # Hash the password before saving
            new_user = User.objects.create(
                name=name,
                email=email,
                password=make_password(password)  # Ensure the password is hashed
            )
            new_user.save()
            messages.success(request, 'You have signed up successfully!')
            return redirect('login')  # Redirect to the login page after signup

    return render(request, 'signup.html')