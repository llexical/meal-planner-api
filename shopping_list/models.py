from django.db import models

"""
Shopping lists should be self contained (sorry model madness)
If you add an item to a shopping list it should handle adding
or removing itself from bring.

There is an API to get the current products in a list so I am going
to use that to check against. If an item is not in the list it will
be added, if its specification is different I will update it.

IMPORTANT NOTE: Via the currently available API that I can work out
if you add something with the same bring_id but different specification
it will override one with the other. On the phone app it does not do this
however the web app you can only add something once which follows the
limitations I've so far met via the API's.
"""

weekday_choices = (
    (0, 'Monday'),
    (1, 'Truesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday')
)

class ShoppingList(models.Model):
    name = models.CharField(max_length=255)
    bring_id = models.CharField(max_length=255, null=True, blank=True)
    day_of_the_week = models.IntegerField(null=True, blank=True, choices=weekday_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


