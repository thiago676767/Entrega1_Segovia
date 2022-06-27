from django.db import models

# Create your models here.
class Telefono(models.Model):
    marca = models.CharField("Marca", max_length=20)
    modelo = models.CharField("Modelo", max_length=30)
    Tipos = (
        ('A', "Analogicos"),
        ('S', "Smartphone"),
        ('C', "Cable"),
    )
    tipo = models.PositiveSmallIntegerField("Tipo", choices=Tipos)
    color = models.CharField("Color", max_length= 20)
    precio = models.FloatField("Precio $")

   

class Auriculares(models.Model):
    marca = models.CharField("Marca", max_length=20)
    Formato = (
        ("Inalambricos"),
        ("Headset"),
        ("Neckband"),
    )


class Televisores(models.Model):
    marca = models.CharField("Marca", max_length=20)
    tamaño = models.IntegerField()