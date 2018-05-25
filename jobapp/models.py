from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#Création du profile utilisateur
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=500)
    about = models.CharField(max_length=1000)
    slogan = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username

# Creation du modèle Job ainsi que la catégorie
class Job(models.Model):
    CATEGORY_CHOICES = (
        ("TR", "Travaux de renovations"),
        ("DM", "Déménagement et manutention"),
        ("NR", "Nettoyage et repassage"),
        ("CL", "Conciergerie et gestion locative"),
        ("BA", "Babysitter et accompagnatrice"),
        ("LV", "Location de voiture"),
        ("IM", "Reparation informatique et autre"),
    )

    title = models.CharField(max_length=500)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=10)
    photo = models.FileField(upload_to='jobs')
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
