from django.urls import path
from . import views

app_name = "fen"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("department/", views.departments_list, name="departments_list"),
    path("specialities/", views.specialities_list, name="specialities_list")
]