from django.db import models
from .validators import validate_nota
from .validators import validate_ci
from django.core.validators import EmailValidator

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50, unique=True, validators=[EmailValidator('Email no valido'),])
    ci = models.CharField(max_length=50, unique=True, validators=[validate_ci,])

    def __str__(self):
        return f"{self.nombre}  {self.apellido} - {self.ci}"


class Asignatura(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)    

    def __str__(self):
        return self.nombre

class Semestre(models.Model):
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo    


class Asignatura_Semestre_Nota(models.Model):
    nota = models.DecimalField(decimal_places=2,max_digits=10, validators=[validate_nota,])
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nota    
    
