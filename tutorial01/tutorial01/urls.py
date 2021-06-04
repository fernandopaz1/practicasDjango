"""tutorial01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),  # agrego todos los paths que hay definidos en polls.url.py y los monto sobre polls/

    # Para acceder a cada respuesta que programo en polls.views.py desde el navegador, hay que agregarle a localhos/polls
    # el path que le configure  en polls.urls.py

    # Ej1.:      index   tiene '' como path   ------> accedo a su respuesta con localhost/polls/   <-- aca hay un string vacio
    # Ej2.:      about  tiene 'about/' como path   ------> accedo a su respuesta con localhost/polls/about/   
]
