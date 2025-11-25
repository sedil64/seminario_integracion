from django.db import models
from .league import League

class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    city = models.CharField(max_length=120, blank=True)
    stadium = models.CharField(max_length=160, blank=True)
    founded_year = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('league', 'name')
        ordering = ('name',)

    def __str__(self):
        return self.name
