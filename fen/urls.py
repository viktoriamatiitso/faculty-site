from django.urls import path
from . import views

app_name = "fen"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("departments/", views.departments_list, name="departments_list"),
    path("programs/", views.specialities_list, name="specialities_list"),
    path("departments/<int:id>/", views.department_detail, name="department_detail"),
    path("programs/<int:id>/", views.speciality_detail, name="speciality_detail"),
]