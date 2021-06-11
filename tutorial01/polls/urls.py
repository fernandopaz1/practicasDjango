from django.urls import path

from . import views


app_name = 'polls'  # para que django no se confunda si tengo 20 apps con un detail cada una 
urlpatterns = [
    path('', views.index, name='index'),  # incluyo la respuesta de views.index en localhost/polls/  <-- despues de polls hay un string vacio
    # el primer campo es el la direccion mediante la cual accedo a la funcion en el navegador
    # esta dirección esta montada sobre el directrio polls/
    path('about/', views.about, name='about'),  # Incluyo la respuesta de views.about en localhost/polls/about

    path('detalle/<int:question_id>/', views.detail, name='detail'),  # añadimos una vista con un path custom segun el question_id
    path('<int:question_id>/results/', views.results, name='results'),  # añadimos una vista con un path custom segun el id que vemos

    #'<int:question_id>/' es lo que queda luego de que urlpatterns le quete la parte de polls ==> identifica el numero que le pasemos en la url
    # como '<int:question_id>/' = '34/' entonces a las vistas le pasa el valor 34

    path('<int:question_id>/vote/', views.vote, name='vote'),  # añadimos una vista con un path custom segun el id que vemos
]

