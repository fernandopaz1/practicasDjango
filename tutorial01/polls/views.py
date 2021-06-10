from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Question

def index(request):  # reques es un objeto tipo HttpRequest ?           
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)  # renderea el template con el contexto que le paso

def about(request):
    return HttpResponse("Soy una página de pruebas!!!")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("La pregunta no existe")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    return HttpResponse("Estas votando la pregunta %s." % question_id)