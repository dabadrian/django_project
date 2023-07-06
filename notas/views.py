from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from .models import Estudiante
from .models import Semestre
from .models import Asignatura
from .models import Asignatura_Semestre_Nota
from .serializers import EstudianteSerializer
from .serializers import AsignaturaSerializer
from .serializers import SemestreSerializer
from .serializers import Asignatura_Semestre_NotaSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import permission_classes
from .permissions import IsDocente
import logging


def index(request):
    return HttpResponse("Hello, world")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

@permission_classes([IsAuthenticated])
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

@permission_classes([IsAdminUser])    
class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer    

@permission_classes([IsAdminUser])
class SemestreViewSet(viewsets.ModelViewSet):
    queryset = Semestre.objects.all()
    serializer_class = SemestreSerializer
    
    
logger = logging.getLogger(__name__)      

@swagger_auto_schema(method='post', request_body=Asignatura_Semestre_NotaSerializer) 
@api_view(["POST"])
@permission_classes([IsDocente])
def enviar_nota(request):
    serializer = Asignatura_Semestre_NotaSerializer(data=request.data)
    if serializer.is_valid():
        logger.info("Operación exitosa")
        serializer.save()
        return JsonResponse({"mensaje": "Nota Registrada Correctamente"}, status=201)
    else:
        return JsonResponse({"mensaje": serializer.errors}, status=400)
        

      