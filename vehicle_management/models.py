from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Marcas"


'''
Tipo vehículo (Coche, Ciclomotor o Motocicleta). 
Chasis. Número identificativo único del Vehículo.
Marca. (Las marcas son un campo que depende de un listado ampliable).
Modelo. (Cadena de texto simple)
Matrícula. (Cadena identificativa única del vehículo)
Color. (Debe poder elegirse de un conjunto predefinido)
Fecha de fabricación. Obligatorio
Fecha Matriculación. Fecha de alta de la matrícula.
Fecha de Baja. Fecha de baja de la matrícula
Suspendido. Flag 
'''


# Create your models here.
class Vehiculo(models.Model):
    TIPO_VEHICULOS_CHOICES = (
        ("COCH", 'Coche'),
        ("CICL", 'Ciclomotor'),
        ("MOTO", 'Motocicleta'),
    )
    COLORES_CHOICES = (
        ("ROJO", 'Rojo'),
        ("VERDE", 'Verde'),
        ("AZUL", 'Azul')
    )
    tipo = models.CharField(choices=TIPO_VEHICULOS_CHOICES, max_length=4)
    chasis = models.IntegerField()
    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    modelo = models.CharField(max_length=100)
    matricula = models.CharField(unique=True, max_length=20)
    color = models.CharField(choices=COLORES_CHOICES, max_length=5)
    fecha_fabricacion = models.DateField()
    fecha_matriculacion = models.DateField()
    fecha_baja = models.DateField()
    suspendido = models.BooleanField(default=False)
