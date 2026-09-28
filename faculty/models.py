from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    head_of_department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Speciality(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=100)
    coordinator_contact = models.CharField(max_length=100)
    graduating_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="specialities")
    subjects_list = models.TextField()
    degree = models.CharField(max_length=100)
    curriculum = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="lecturers")

    def __str__(self):
        return self.name

class HomePage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.title