from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escolar.views import AlumnoViewSet, MateriaViewSet, CalificacionViewSet

router = DefaultRouter()
router.register('alumnos', AlumnoViewSet)
router.register('materias', MateriaViewSet)
router.register('calificaciones', CalificacionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]