from django.db import models
from django.db.models import Count


class RealEstateListingManager(models.Manager):
    def by_property_type(self, property_type):
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price, max_price):
        return self.filter(price__range=(min_price, max_price))

    def with_bedrooms(self, bedrooms_count):
        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self):
        # Using annotate and order_by to get the most visited locations
        # Order by the count of records in descending order
        # Then order by the id of the location in ascending order
        return (
            self.values('location')
            .annotate(location_count=Count('id'))
            .order_by('-location_count', 'location')[:2]
        )


class VideoGameManager(models.Manager):
    def games_by_genre(self, genre):
        return self.filter(genre=genre)

    def recently_released_games(self, year):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        highest_rating = self.aggregate(models.Max('rating'))['rating__max']
        if highest_rating is not None:
            return self.filter(rating=highest_rating).first()
        return None

    def lowest_rated_game(self):
        lowest_rating = self.aggregate(models.Min('rating'))['rating__min']
        if lowest_rating is not None:
            return self.filter(rating=lowest_rating).first()
        return None

    def average_rating(self):
        avg_rating = self.aggregate(models.Avg('rating'))['rating__avg']
        if avg_rating is not None:
            return format(avg_rating, '.1f')
        return None