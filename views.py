from django.http import HttpResponse
from rest_framework import viewsets
from .models import Medico, Paciente, Cita, Notificacion, Sucursal, Usuario
from .serializers import (
    MedicoSerializer,
    PacienteSerializer,
    CitaSerializer,
    NotificacionSerializer,
    SucursalSerializer,
    UsuarioSerializer,
)


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer


class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


def home(request):
    return HttpResponse("Bienvenido a MedAgenda")
