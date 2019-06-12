from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question, Choice

# Create your views here.

def index(request):
    question_list = Question.objects.order_by('pubDate')
    context = {
        'message' : True,
        'questionData' : question_list 
    }
    return render(request, 'polls/index.html' , context)

def details(request , question_id):
    try:
        question = Choice.objects.get(pk=question_id)
    except:
        raise Http404("Question doesn't exist")
    return render(request, 'polls/details.html' , context = {'question': question})

def results(request , question_id):
    return HttpResponse("You're looking at the results %s." % question_id)

def vote(request , question_id):
    return HttpResponse("You're voting at question %s." % question_id)