from django.contrib import admin

from .models import Department, ExchangeProgram, HomePage, Lecturer, Speciality

# Register your models here.

admin.site.register(Department)
admin.site.register(Speciality)
admin.site.register(Lecturer)
admin.site.register(HomePage)
admin.site.register(ExchangeProgram)
