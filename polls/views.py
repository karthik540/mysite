from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.

def index(request):
    question_list = Question.objects.order_by('pubDate')
    context = {
        'message' : True,
        'questionData' : question_list 
    }
    return render(request, 'polls/index.html' , context)

def details(request , question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request , question_id):
    return HttpResponse("You're looking at the results %s." % question_id)

def vote(request , question_id):
    return HttpResponse("You're voting at question %s." % question_id)