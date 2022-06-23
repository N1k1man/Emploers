from django.shortcuts import render
from .models import Employer, Visit


def index(request):
    employers = Employer.objects.all()
    context = {
        'employers': employers
    }
    return render(request, 'show.html', context)


def get_employer(request, slug):
    visit = Visit.objects.filter(employer__slug=slug)
    employer = Employer.objects.get(slug=slug)
    context = {
        'visits': visit,
        'employer': employer
    }
    return render(request, 'get_employer.html', context)
