from django.shortcuts import render, redirect
from .models import HomePage, Department, Speciality

# Create your views here.

def home_page(request):
    content = HomePage.objects.first()
    return render(request, "faculty/home_page.html", {"content": content})

def departments_list(request):
    content = HomePage.objects.first()
    departments = Department.objects.all()
    return render(request, "faculty/departments_list.html", {"departments": departments, "content": content})

def specialities_list(request):
    content = HomePage.objects.first()
    specialities = Speciality.objects.all()
    return render(request, "faculty/specialities_list.html", {"specialities": specialities, "content": content})

def department_detail(request,id):
    content = HomePage.objects.first()
    try:
        department = Department.objects.get(id=id)
    except Department.DoesNotExist:
        return redirect("faculty:departments_list")
    return render(request, "faculty/department_detail.html", {"department": department, "content": content})

def speciality_detail(request,id):
    content = HomePage.objects.first()
    try:
        speciality = Speciality.objects.get(id=id)
    except Speciality.DoesNotExist:
        return redirect("faculty:specialities_list")
    return render(request, "faculty/speciality_detail.html", {"speciality": speciality, "content": content})