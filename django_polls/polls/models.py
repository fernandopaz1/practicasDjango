# Create your models here.
from django.db import models
import datetime
from django.contrib import admin
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)  #Estas instancias se traducirán en columnas de la base de dats
                                                                                        # creo que no conviene usar camelCase sino snake_case
                                                                                        # el tipo de dato se los da CharField (la base necesita que le
                                                                                        # espcifiquemos tipos de datos)
                                                                                        # La pk es el numero de clase ??????
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


    @admin.display(
        boolean=True,     # con esto me muestra un tick en vez de true
        ordering='pub_date', # me los ordena por pub_date
        description = 'Published recently?', # es el nombrre de la columna
    )

    def was_published_recently(self):
        now = timezone.now()
        return  timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # esto esta relacionado a questions ya que tiene como FK
                                                                                                                    # Questions 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


    # para que me tome estos modelos en la base de datos, hay que agregar polls a las settings del proyecto