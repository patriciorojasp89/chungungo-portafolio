from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Step
from .forms import StepForm


class StepListView(ListView):
    model = Step
    template_name = "chungungo/step_list.html"
    context_object_name = "steps"


class StepCreateView(LoginRequiredMixin, CreateView):
    model = Step
    form_class = StepForm
    template_name = "chungungo/step_form.html"
    success_url = reverse_lazy("chungungo:step_list")
    login_url = reverse_lazy("login")