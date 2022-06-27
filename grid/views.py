from django.shortcuts import render
from .models import Employer, Visit
from datetime import date


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


def get_visit_day(request):
    day = date.today()
    visits = Visit.objects.filter(date=day)
    if request.method == 'POST':
        day = request.POST['day']
        visit = Visit.objects.filter(date=day)
    context = {
        'visits': visits,
        'day': day
    }

    return render(request, 'get_visit_day.html', context)


def add_visit(request):
    employers = Employer.objects.all()
    if request.method == 'POST':
        date = request.POST['date']
        employer = request.POST['employer']
        visited = request.POST['visited']
        time_start = request.POST['time_start']
        time_end = request.POST['time_end']
        reason = request.POST['reason']

        visit = Visit(date=date, employer=Employer.objects.get(slug=employer), visited=visited, time_start=time_start, time_end=time_end, reason=reason)
        visit.save()
    context = {
        'employers': employers
    }
    return render(request, 'add_visit.html', context)


