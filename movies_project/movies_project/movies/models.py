from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    minimum_age = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name