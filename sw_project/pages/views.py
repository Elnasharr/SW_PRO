from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import University, Scholarship

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())


def scholarship_details(request):
    template = loader.get_template('scholarship-details.html')
    return HttpResponse(template.render())


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


def university_details(request):
    template = loader.get_template('university-details.html')
    return HttpResponse(template.render())