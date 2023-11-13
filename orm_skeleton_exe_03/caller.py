import os
import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions

from main_app.models import Pet, Artifact, Location, Car, Task
from populate_db import populate_model_with_data


def create_pet(name: str, species: str) -> str:
    Pet.objects.create(
        name=name,
        species=species,
    )

    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {artifact.name} is {age} years old!"


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()


def show_all_locations():
    locations = Location.objects.all().order_by('-id')
    return '\n'.join(str(loc) for loc in locations)


def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals():
    capitals = Location.objects.filter(is_capital=True).values('name')
    return capitals


def delete_first_location():
    location = Location.objects.first()
    if location:
        location.delete()


def apply_discount() -> None:
    cars = Car.objects.all()

    for car in cars:
        percentage = sum(int(x) for x in str(car.year)) / 100
        discount = float(car.price) * percentage
        car.price_with_discount = float(car.price) - discount
        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


def show_unfinished_tasks() -> str:
    unfinished_tasks = Task.objects.filter(is_finished=False)

    return '\n'.join(str(t) for t in unfinished_tasks)


def complete_odd_tasks() -> None:
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str) -> None:
    tasks_with_matching_title = Task.objects.filter(title=task_title)
    decoded_text = ''.join(chr(ord(x) - 3) for x in text)
    # Task.objects.filter(title=task_title).update(description=decoded_text)

    for task in tasks_with_matching_title:
        task.description = decoded_text
        task.save()