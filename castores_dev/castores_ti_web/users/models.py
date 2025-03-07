from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Definir relaciones con related_name para evitar el conflicto
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',  # Cambia el nombre del reverse accessor
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_user_permissions',  # Cambia el nombre del reverse accessor
        blank=True,
    )