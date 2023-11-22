from django.db import models


class ProfileManager(models.Manager):
    def get_regular_customers(self):
        """
        Retrieve and return all profile objects with more than two orders.
        Order profiles by the number of orders in descending order.
        """
        # Annotate the profiles with the count of their orders
        profiles_with_order_count = self.annotate(order_count=models.Count('order'))

        # Filter profiles with more than two orders
        regular_customers = profiles_with_order_count.filter(order_count__gt=2)

        # Order profiles by the number of orders in descending order
        regular_customers = regular_customers.order_by('-order_count')

        return regular_customers