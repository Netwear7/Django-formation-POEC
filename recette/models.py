from django.db import models


# temporary
# recette = [
#     {'name': 'Salade', 'price': 5.50, 'ingredients': 'salade, tomates cerise, oeuf, maïs, vinaigrette'},
#     {'name': 'Sandwich signature', 'price': 8.45, 'ingredients': 'salade, tomates, oignons rouge, sauce, wagyu'},
#     {'name': 'Moule frite', 'price': 15, 'ingredients': 'moule, maroille, céléri, vin blanc, frite'},
#     {'name': 'Welsh', 'price': 12.99, 'ingredients': 'cheddar, pain, moutard, jambon, oeuf'},
# ]

# Create your models here.
class Recette(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    ingredients = models.TextField()

    def __str__(self):
        return self.name
