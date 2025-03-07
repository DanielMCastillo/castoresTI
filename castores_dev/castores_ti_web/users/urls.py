from django.urls import path
from django.contrib.auth import views as auth_views  # Importamos las vistas de autenticación
from . import views

urlpatterns = [
    # Otras rutas de tu proyecto
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/listar/', views.listar_usuarios, name='listar_usuarios'),
]
