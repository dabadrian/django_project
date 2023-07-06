from django.contrib import admin

# Register your models here.
from .models import Estudiante
from .models import Semestre
from .models import Asignatura
from .models import Asignatura_Semestre_Nota

admin.site.register(Estudiante)
admin.site.register(Semestre)
admin.site.register(Asignatura)
admin.site.register(Asignatura_Semestre_Nota)
