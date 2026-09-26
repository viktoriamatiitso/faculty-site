from django.shortcuts import render
from .models import HomePage, Department, Speciality

# Create your views here.

def home_page(request):
    content = HomePage.objects.first()
    return render(request, "fen/home_page.html", {"content": content})

def departments_list(request):
    departments = Department.objects.all()
    return render(request, "fen/departments_list.html", {"departments": departments})

def specialities_list(request):
    specialities = Speciality.objects.all()
    return render(request, "fen/specialities_list.html", {"specialities": specialities})