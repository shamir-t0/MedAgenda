from django.db import models


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita {self.id} - {self.fecha}"


class Notificacion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField()

    def __str__(self):
        return f"Notificación {self.id}"


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
