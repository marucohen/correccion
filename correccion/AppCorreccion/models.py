from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return f"Nombre: {self.nombre}"   
    


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.avatar}"