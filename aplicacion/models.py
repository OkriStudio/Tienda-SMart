from django.db import models
from django.core.validators import MinValueValidator
from datetime import date

from django.db import models
from django.core.validators import MinValueValidator

class Producto(models.Model):
    ALIMENTOS_CHOICES = [
        ('Envasado', 'Productos envasados'),
        ('Fruta', 'Manzana, Platano, Kiwi, etc'),
        ('Verduras', 'Palta, Lechuga, Zanahoria, etc'),
        ('Carnes', 'Vacuno, Cerdo, Pollo, etc'),
    ]
    
    nombre = models.CharField(max_length=50, verbose_name='Nombre de la verdura')
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='Precio', 
        validators=[MinValueValidator(0,message="El valor no puede ser negativo")]
    )
    tipo_alimento = models.CharField(
        max_length=10,
        choices=ALIMENTOS_CHOICES, 
        verbose_name='Tipo de alimento'
    )
    fecha_caducidad = models.DateField(verbose_name='Fecha de caducidad')

    def __str__(self):
        return self.nombre



ESTADO_CHOICES = [
    (1, 'Activo'),
    (2, 'Inactivo')
]

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    correo = models.EmailField(max_length=50)
    estado = models.IntegerField(
        choices=ESTADO_CHOICES
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Tienda(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='sistemas') 
    nombre_distribuidora = models.CharField(max_length=100, verbose_name='Nombre de la Distribuidora')
    descuento = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Descuento (%)')
    productos = models.ManyToManyField(Producto, related_name='sistemas') 

    def __str__(self):
        return self.nombre_distribuidora
