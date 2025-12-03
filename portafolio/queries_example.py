from django.db import connection
from django.utils import timezone
from .models import Proyecto, Skill, Contacto, TareaProyecto, PerfilUsuario


def crear_datos_demo():
    python = Skill.objects.create(nombre="Python", nivel="avanzado")
    django = Skill.objects.create(nombre="Django", nivel="intermedio")
    js = Skill.objects.create(nombre="JavaScript", nivel="intermedio")

    portafolio = Proyecto.objects.create(
        titulo="Portafolio Personal",
        descripcion="Sitio web con mis proyectos",
        url_demo="https://mi-demo.com",
        url_codigo="https://github.com/miuser/mi-portafolio",
        esta_activo=True,
    )
    kanban = Proyecto.objects.create(
        titulo="Chungungo Kanban",
        descripcion="Aplicación de tablero Kanban",
        esta_activo=True,
    )


    portafolio.skills.add(python, django, js)
    kanban.skills.add(python, django)


    contacto = Contacto.objects.create(
        nombre="Juan Pérez",
        correo="juan@example.com",
        mensaje="Hola, me interesa tu trabajo.",
    )
    PerfilUsuario.objects.create(
        contacto=contacto,
        telefono="+56912345678",
        ciudad="Santiago",
    )


    TareaProyecto.objects.create(
        proyecto=kanban,
        titulo="Configurar modelos Django",
        completada=True,
    )
    TareaProyecto.objects.create(
        proyecto=kanban,
        titulo="Crear vistas y templates",
        completada=False,
    )
    TareaProyecto.objects.create(
        proyecto=portafolio,
        titulo="Diseñar la página principal",
        completada=False,
    )


def ejemplos_basicos_orm():
    proyectos_activos = Proyecto.objects.filter(esta_activo=True)
    proyectos_kanban = Proyecto.objects.filter(titulo__icontains="kanban")
    skills_avanzadas = Skill.objects.filter(nivel="avanzado")
    proyectos_no_inactivos = Proyecto.objects.exclude(esta_activo=False)
    try:
        portafolio = Proyecto.objects.get(titulo="Portafolio Personal")
    except Proyecto.DoesNotExist:
        portafolio = None
    except Proyecto.MultipleObjectsReturned:
        portafolio = None
    tareas_ordenadas = TareaProyecto.objects.order_by("titulo")
    hoy = timezone.localdate()
    contactos_hoy = Contacto.objects.filter(creado_en__date=hoy)

    return {
        "proyectos_activos": proyectos_activos,
        "proyectos_kanban": proyectos_kanban,
        "skills_avanzadas": skills_avanzadas,
        "proyectos_no_inactivos": proyectos_no_inactivos,
        "portafolio": portafolio,
        "tareas_ordenadas": tareas_ordenadas,
        "contactos_hoy": contactos_hoy,
    }


def ejemplo_sql_crudo():
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, titulo, esta_activo
            FROM portfolio_proyecto
            WHERE esta_activo = %s
            """,
            [True],
        )
        filas = cursor.fetchall()
    return filas
