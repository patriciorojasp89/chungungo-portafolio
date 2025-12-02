from django.urls import path
from .views import StepListView, StepCreateView

app_name = "chungungo"

urlpatterns = [
    path("", StepListView.as_view(), name="step_list"),
    path("nuevo/", StepCreateView.as_view(), name="step_create"),
]
