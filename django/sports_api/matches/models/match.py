from django.db import models
from leagues.models import Team, League

class Match(models.Model):
    STATUS_SCHEDULED = 'SCHEDULED'
    STATUS_PLAYING = 'PLAYING'
    STATUS_FINISHED = 'FINISHED'

    STATUS_CHOICES = [
        (STATUS_SCHEDULED, 'Programado'),
        (STATUS_PLAYING, 'En juego'),
        (STATUS_FINISHED, 'Finalizado'),
    ]

    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='matches')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    match_date = models.DateTimeField()
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_SCHEDULED)

    home_score = models.PositiveIntegerField(default=0)
    away_score = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-match_date',)

    def __str__(self):
        return f'{self.home_team} vs {self.away_team} ({self.league})'
