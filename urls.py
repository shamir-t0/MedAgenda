from .views import home
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MedicoViewSet,
    PacienteViewSet,
    CitaViewSet,
    NotificacionViewSet,
    SucursalViewSet,
    UsuarioViewSet,
)

router = DefaultRouter()
router.register(r'medicos', MedicoViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'citas', CitaViewSet)
router.register(r'notificaciones', NotificacionViewSet)
router.register(r'sucursales', SucursalViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns = [
    path('', home, name='home'),
    # aquí otras rutas si tienes
]
