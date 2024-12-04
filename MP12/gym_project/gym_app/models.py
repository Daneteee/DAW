from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('user', 'Usuari del Gimnàs'),
        ('trainer', 'Entrenador'),
        ('director', 'Director')
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    REQUIRED_FIELDS = ['role']
    USERNAME_FIELD = 'email'
    
    
class Routine(models.Model):
    trainer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'trainer'}
    )
    name = models.CharField(max_length=255)
    exercises = models.TextField()
    duration = models.DurationField()
    recommendations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=[
        ('Dilluns', 'Dilluns'),
        ('Dimarts', 'Dimarts'),
        ('Dimecres', 'Dimecres'),
        ('Dijous', 'Dijous'),
        ('Divendres', 'Divendres'),
    ])
    time = models.TimeField()
    room = models.CharField(max_length=255, default="Sala Principal")

    class Meta:
        unique_together = ('day', 'time', 'room') 

    def __str__(self):
        return f"{self.routine.name} - {self.day} a las {self.time}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    
    