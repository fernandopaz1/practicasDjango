from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)  #Estas instancias se traducirán en columnas de la base de dats
                                                                                        # creo que no conviene usar camelCase sino snake_case
                                                                                        # el tipo de dato se los da CharField (la base necesita que le
                                                                                        # espcifiquemos tipos de datos)
                                                                                        # La pk es el numero de clase ??????
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # esto esta relacionado a questions ya que tiene como FK
                                                                                                                    # Questions 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # para que me tome estos modelos en la base de datos, hay que agregar polls a las settings del proyecto