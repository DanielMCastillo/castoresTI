from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.apps import apps

@receiver(post_migrate)
def create_roles(sender, **kwargs):
    Group = apps.get_model("auth", "Group")  # Obtiene el modelo Group de manera segura
    Permission = apps.get_model("auth", "Permission")  # Obtiene permisos de manera segura

    admin_group, created = Group.objects.get_or_create(name="Administrador")
    almacenista_group, created = Group.objects.get_or_create(name="Almacenista")

    # Asigna permisos según tu modelo
    permisos_admin = [
        "lista_productos",
        "agregar_producto",
        "aumentar_inventario",
        "cambiar_estatus_producto",
    ]

    permisos_almacenista = [
        "lista_productos",
        "salida_producto",
    ]

    for permiso_codename in permisos_admin:
        permiso = Permission.objects.filter(codename=permiso_codename).first()
        if permiso:
            admin_group.permissions.add(permiso)

    for permiso_codename in permisos_almacenista:
        permiso = Permission.objects.filter(codename=permiso_codename).first()
        if permiso:
            almacenista_group.permissions.add(permiso)

    print("✅ Grupos y permisos creados exitosamente.")

