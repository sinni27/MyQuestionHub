from django.shortcuts import render
from . models import Topic,Question

# Create your views here.

def index(request):
    all_questions = Question.objects.all()
    return render(request,'questions/index.html',{'all_questions':all_questions})


def detail(request,question_id):
    ques = Question.objects.get(pk=question_id)
    return render(request,'questions/detail.html',{'ques':ques})
