from django.db import models
from django.db.models.constraints import UniqueConstraint


class Articles(models.Model):
    """Model of Articles"""
    text = models.TextField('Article')
    time = models.DateTimeField('Time add')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Teams(models.Model):
    """Model of Teams"""
    team = models.CharField('Team', max_length=25)
    logo = models.ImageField(upload_to='logos')

    """Define direction of images for this class"""
    @property
    def photo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url

    def __str__(self):
        return f"{self.team}"

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class Matches(models.Model):
    """Model of Matches"""
    team1 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='+')
    team2 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='+')
    time = models.DateTimeField('Time', max_length=50)

    def __str__(self):
        return f"{self.time} {self.team1}-{self.team2}"

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'
        constraints = [
            UniqueConstraint(fields=['team1', 'team2'], name='unique_match')    # each match have to be unique
        ]


class Cards(models.Model):
    """Model of Cards"""
    image = models.ImageField(upload_to='cards')
    name = models.CharField('Name', max_length=15)
    description = models.TextField('Description')

    """Define direction of images for this class"""
    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return f" {self.name}"

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
