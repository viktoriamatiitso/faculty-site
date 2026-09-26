from django.shortcuts import render
from .models import HomePage

# Create your views here.

def home_page(request):
    content = HomePage.objects.first()
    return render(request, "fen/home_page.html", {"content": content})

def departments_list(request):
    return render(request, "fen/departments_list.html")

def specialities_list(request):
    return render(request, "fen/specialities_list.html")