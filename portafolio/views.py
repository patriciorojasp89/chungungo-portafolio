from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto
from .forms import ProyectoForm


def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    context = {"proyectos": proyectos}
    return render(request, "portafolio/lista_proyectos.html", context)


def crear_proyecto(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_proyectos")
    else:
        form = ProyectoForm()

    context = {"form": form}
    return render(request, "portafolio/crear_proyecto.html", context)


def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)

    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect("lista_proyectos")
    else:
        form = ProyectoForm(instance=proyecto)

    context = {"form": form, "proyecto": proyecto}
    return render(request, "portafolio/editar_proyecto.html", context)


def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)

    if request.method == "POST":
        proyecto.delete()
        return redirect("lista_proyectos")

    context = {"proyecto": proyecto}
    return render(request, "portafolio/confirmar_eliminar_proyecto.html", context)
