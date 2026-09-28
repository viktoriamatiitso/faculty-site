from django.shortcuts import render, redirect
from .models import HomePage, Department, Speciality

# Create your views here.

def home_page(request):
    content = HomePage.objects.first()
    return render(request, "faculty/home_page.html", {"content": content})

def departments_list(request):
    departments = Department.objects.all()
    return render(request, "faculty/departments_list.html", {"departments": departments})

def specialities_list(request):
    specialities = Speciality.objects.all()
    return render(request, "faculty/specialities_list.html", {"specialities": specialities})

def department_detail(request,id):
    try:
        department = Department.objects.get(id=id)
    except Department.DoesNotExist:
        return redirect("faculty:departments_list")
    return render(request, "faculty/department_detail.html", {"department": department})

def speciality_detail(request,id):
    try:
        speciality = Speciality.objects.get(id=id)
    except Speciality.DoesNotExist:
        return redirect("faculty:specialities_list")
    return render(request, "faculty/speciality_detail.html", {"speciality": speciality})