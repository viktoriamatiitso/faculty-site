from django.shortcuts import render, redirect
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

def department_detail(request,id):
    try:
        department = Department.objects.get(id=id)
    except Department.DoesNotExist:
        return redirect("fen:departments_list")
    return render(request, "fen/department_detail.html", {"department": department})