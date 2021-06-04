from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # incluyo la respuesta de views.index en localhost/polls/  <-- despues de polls hay un string vacio
    # el primer campo es el la direccion mediante la cual accedo a la funcion en el navegador
    # esta dirección esta montada sobre el directrio polls/
    path('about/', views.about, name='about'),  # Incluyo la respuesta de views.about en localhost/polls/about
]