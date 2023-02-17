from django.urls import path
from . import views

urlpatterns = [
    path ('hola/<str:nombre>', views.saludar)
]