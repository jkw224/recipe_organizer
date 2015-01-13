from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, default="This is a default description", help_text="This is a quick description of your recipe")
    directions = models.TextField(default="Add Directions", help_text="Steps to make the recipe")
    ingredients = models.TextField(blank=True, null=True, default="Add ingredients!", help_text="Ingredients to add")
    delicious = models.TextField(blank=True, null=True, default='This is a default "this is delicious" checkbox', help_text="This is a quick description of your recipe")
    date_created = models.TextField(default="This is a default date_created", help_text="This is a quick description of your recipe")
    # email = models.TextField(default="This is a default email field", help_text="This is a quick description of your recipe")
    # url = models.TextField(default="This is a default url field", help_text="This is a quick description of your recipe")


    def __str__(self):
        return self.name