from django.shortcuts import render, get_object_or_404
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

def details(request, question_id):
    questionObject = get_object_or_404(Question, pk=question_id)
    data = {
        'id': questionObject.id,
        'choiceList': questionObject.choice_set.all(),
        'question': questionObject.questionText
    }
    print(data)
    return render(request, 'polls/details.html', {'data': data})

def results(request , question_id):
    return HttpResponse("You're looking at the results %s." % question_id)

def vote(request , question_id):
    return HttpResponse("You're voting at question %s." % question_id)