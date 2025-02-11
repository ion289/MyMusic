from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, OneToOneField, TextField


# Create your models here.
class Profile(models.Model):
    biography = TextField()

    # OneToOneField inseamna ca fiecare User are un singure Profile si vice-versa
    # on_delete=CASCADE inseamna ca atunci cand se sterge un User
    # Profile-ul asociat acelui User sa va sterge si el automat
    user = OneToOneField(User, on_delete=CASCADE)

    def __str__(self):
        return f'Profilul lui {self.user.username}'