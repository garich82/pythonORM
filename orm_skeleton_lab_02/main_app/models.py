from django.db import models

# Create your models here.

CITIES = [
    ('Sofia', 'Sofia'),
    ('Burgas', 'Burgas'),
    ('Plovdiv', 'Plovdiv'),
    ('Varna', 'Varna')
]


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)


class Department (models.Model):
    code = models.CharField(max_length=4, primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True)
    employees_count = models.PositiveIntegerField(verbose_name="Employees Count", default=1)
    location = models.CharField(max_length=20, choices=CITIES, null=True, blank=True)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)


class Project(models.Model):
