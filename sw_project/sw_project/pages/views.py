from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import University, Scholarship

# Create your views here.
def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def scholarship_details(request, scholarship_id):
   
    scholarship = get_object_or_404(Scholarship, id=scholarship_id)
    context = {
        'scholarship': scholarship,
    }
    return render(request, 'scholarship-details.html', context)


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


def university_details(request, university_id):
    university = get_object_or_404(University, id=university_id)
    context = {
        'university': university,
    }
    return render(request, 'university-details.html', context)
