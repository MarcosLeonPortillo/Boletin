from django.db import models


# Create your models here.
class Vehiculo(models.Model):
    TIPO_VEHICULOS_CHOICES = (
        ("COCH", 'Coche'),
        ("CICL", 'Ciclomotor'),
        ("MOTO", 'Motocicleta    '),
    )
    tipo_vehiculo = models.CharField(choices=TIPO_VEHICULOS_CHOICES, max_length=4)
    chasis = models.IntegerField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    matricula = models.CharField(unique=True, max_length=20)
