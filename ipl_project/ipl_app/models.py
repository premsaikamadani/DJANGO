from django.db import models

# Create your models here.
class Franchise(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    founded_year = models.IntegerField()
    no_of_trophies = models.IntegerField()
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    city = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)

    class Meta:
        db_table = 'franchises'

    def __str__(self):
        return f"{self.name} ({self.short_name})"



class Player(models.Model):
    ROLE_CHOICES = [
        ('Batsman', 'Batsman'),
        ('Bowler', 'Bowler'),
        ('All-Rounder', 'All-Rounder'),
        ('Wicket-Keeper', 'Wicket-Keeper'),
    ]
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    role = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='players/', blank=True, null=True)

    class Meta:
        db_table = 'players'

    def __str__(self):
        return f"{self.name} ({self.role})"
