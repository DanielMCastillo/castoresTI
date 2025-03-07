from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Producto(models.Model):
    ESTATUS_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.IntegerField(default=0)  # Inventario inicia en 0
    estatus = models.CharField(max_length=10, choices=ESTATUS_CHOICES, default='activo')

    def __str__(self):
        return self.nombre
    
    
class SalidaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_salida = models.IntegerField()
    fecha_salida = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Asegurar que la cantidad no sea None y tenga un valor predeterminado de 0
        if self.producto.cantidad is None:
            self.producto.cantidad = 0  # Asignar 0 si la cantidad es None

        # Verificar que no se retire más cantidad de la disponible
        if self.cantidad_salida > self.producto.cantidad:
            raise ValidationError(
                f"No puedes retirar {self.cantidad_salida} unidades. Solo hay {self.producto.cantidad} disponibles."
            )
            
    def save(self, *args, **kwargs):
        self.clean()  # Llamamos la validación antes de guardar
        self.producto.cantidad -= self.cantidad_salida
        self.producto.save()
        super().save(*args, **kwargs)


class MovimientoProducto(models.Model):
    TIPOS_MOVIMIENTO = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='producto_id')
    tipo_movimiento = models.CharField(max_length=7, choices=TIPOS_MOVIMIENTO)
    cantidad = models.PositiveIntegerField()
    realizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # El usuario que realizó el movimiento
    fecha_hora = models.DateTimeField(auto_now_add=True)  # Fecha y hora del movimiento

    def __str__(self):
        return f"{self.tipo_movimiento} - {self.producto.nombre} - {self.cantidad} unidades"