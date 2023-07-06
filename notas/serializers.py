from rest_framework import serializers

from .models import Estudiante
from .models import Semestre
from .models import Asignatura
from .models import Asignatura_Semestre_Nota

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = "__all__"
        
class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = "__all__"        
        
class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semestre
        fields = "__all__"         


class Asignatura_Semestre_NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura_Semestre_Nota
        fields = "__all__"           
        
        