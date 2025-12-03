from django.contrib import admin
from .models import Proyecto, Skill, Contacto, PerfilUsuario, TareaProyecto


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "esta_activo", "fecha_creacion")
    list_filter = ("esta_activo", "fecha_creacion")
    search_fields = ("titulo", "descripcion")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nivel")
    list_filter = ("nivel",)
    search_fields = ("nombre",)


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo", "creado_en")
    search_fields = ("nombre", "correo")


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ("contacto", "telefono", "ciudad")
    search_fields = ("contacto__nombre", "ciudad")


@admin.register(TareaProyecto)
class TareaProyectoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "proyecto", "completada")
    list_filter = ("completada", "proyecto")
    search_fields = ("titulo",)
