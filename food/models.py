from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.CharField(
        max_length=500,
        default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg",
    )

    def __str__(self):
        return self.name
