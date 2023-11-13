import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import Lecturer, LecturerProfile

lecturer = Lecturer.objects.get(first_name='John', last_name="Doe")

lecturer_profile_from_db = LecturerProfile.objects.get(email='john.doe@university.lecturers.com')

print(f"{lecturer_profile_from_db.lecturer.first_name} {lecturer_profile_from_db.lecturer.last_name} has a profile.")
