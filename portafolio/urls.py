from django.urls import path
from . import views

urlpatterns = [
    path("proyectos/", views.lista_proyectos, name="lista_proyectos"),
    path("proyectos/nuevo/", views.crear_proyecto, name="crear_proyecto"),
    path("proyectos/<int:pk>/editar/", views.editar_proyecto, name="editar_proyecto"),
    path("proyectos/<int:pk>/eliminar/", views.eliminar_proyecto, name="eliminar_proyecto"),
]
