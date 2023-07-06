from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"estudiantes", views.EstudianteViewSet)
router.register(r"asignaturas", views.AsignaturaViewSet)
router.register(r"semestres", views.SemestreViewSet)

urlpatterns = [
    path("contact/<str:name>", views.contact),
    path("nota", views.enviar_nota, name="enviar-nota"),
    path("", include(router.urls)),
]
