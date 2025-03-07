from django.urls import path
from .views import agregar_producto, lista_productos, aumentar_inventario, cambiar_estatus_producto, salida_producto, registrar_movimiento, listar_movimientos

urlpatterns = [
    path('productos/', lista_productos, name='lista_productos'),
    path('productos/agregar/', agregar_producto, name='agregar_producto'),
    path('productos/aumentar/<int:producto_id>/', aumentar_inventario, name='aumentar_inventario'),
    path('productos/cambiar-estatus/<int:producto_id>/', cambiar_estatus_producto, name='cambiar_estatus_producto'),
    path('productos/salida_producto/', salida_producto, name='salida_producto'),
    path('productos/registro_mov/', registrar_movimiento, name='registrar_movimiento'),
    path('productos/historial_movs/', listar_movimientos, name='listar_movimientos'),
]
