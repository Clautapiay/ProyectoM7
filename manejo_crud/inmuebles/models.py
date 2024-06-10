from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError



# Create your models here.
# def validate_min_value(value): #otra forma de validad en el modelo
#     if value < 0:
#         raise ValidationError(
#             "El Valor debe ser Positivo"
#         )

class Usuario(models.Model):
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_usuario.username

class Inmueble(models.Model):
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    nombre_inmueble = models.CharField(max_length=100, null=False, blank=False)    
    descripcion = models.TextField(null=False, blank=False, default='')
    m2_construidos = models.FloatField(null=False, default=0.0)
    m2_totales = models.FloatField(null=False, default=0.0)
    cantidad_estacionamientos = models.PositiveIntegerField(default=0)
    cantidad_habitaciones = models.PositiveIntegerField(default=0)
    cantidad_baños = models.PositiveIntegerField(default=0)
    direccion = models.CharField(max_length=100, null=False, blank=False) 
    id_comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE)
    id_tipo_de_inmueble = models.ForeignKey('Tipo_de_inmueble', on_delete=models.CASCADE) #casa/depto/parcela
    precio_mensual_arriendo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nombre_inmueble

class Region(models.Model):
    region = models.CharField()
    def __str__(self):
        return self.region



class Comuna(models.Model):
    comuna  = models.CharField()
    def __str__(self):
        return self.comuna 

class Tipo_de_inmueble(models.Model): #dpto, casa, parcela
    # CHOICES = [
    #     ('Departamento', 'Departamento'),
    #     ('Casa', 'Casa'),
    #     ('Parcela', 'Parcela'),
    # ]
    tipo_de_inmueble = models.TextField()
# ID 1. Dpto 2. Casa 3. Parcela
    def __str__(self):
        return self.tipo_de_inmueble

class Tipo_de_usuario(models.Model): #arrendatario -- arrendador 
    CHOICES = [
        ('Arrendador', 'Arrendador'),
        ('Arrendatario', 'Arrendatario'),
    ]
    tipo_de_usuario = models.CharField(choices=CHOICES)

    def __str__(self):
        return self.tipo_de_usuario
        #(self.pk) +'-'+

class Perfil(models.Model): #para interactuar
    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    rut = models.CharField(max_length=50, primary_key=True, null=False)
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    telefono_personal = models.CharField(max_length=50)
    correo_electronico = models.CharField(max_length=50)
    tipo_de_usuario = models.ForeignKey('Tipo_de_usuario', on_delete=models.CASCADE) #arrendatario/arrendador

    def __str__(self):
        return self.usuario.username    