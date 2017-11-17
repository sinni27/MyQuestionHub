from django.shortcuts import render
from . models import Topic,Question
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
# def index(request):
#     all_questions = Question.objects.all()
#     return render(request,'questions/index.html',{'all_questions':all_questions})
#
#
# def detail(request,question_id):
#     ques = Question.objects.get(pk=question_id)
#     return render(request,'questions/detail.html',{'ques':ques})
#Generic views
class IndexView(generic.ListView):
    template_name = 'questions/index.html'
    context_object_name = 'all_questions'

    def get_queryset(self):
        return Question.objects.all()

class TopicDetailView(generic.DetailView):
    model = Topic
    template_name = 'questions/topic_detail.html'

    context_object_name = 'top'

    def get_queryset(self):
        return Topic.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'questions/detail.html'

    context_object_name = 'ques'

    def get_queryset(self):
        return Question.objects.all()



class TopicCreate(CreateView):
    model = Topic
    fields = ['topic_name','related_to']



class QuestionCreate(CreateView):
    model = Question
    fields = ['posted_by','topic','content']

class QuestionUpdate(UpdateView):
    model = Question
    fields = ['posted_by','topic','content']


class QuestionDelete(DeleteView):
    model = Question
    fields = ['posted_by','topic','content']
    success_url = reverse_lazy('questions:index')
