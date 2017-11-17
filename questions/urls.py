from django.conf.urls import url
from . import views
app_name = 'questions'


urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^topic_detail/(?P<pk>[0-9]+)/$',views.TopicDetailView.as_view(),name='topic_detail'),

    #/questions/topic/add/
    url(r'topic/add/$',views.TopicCreate.as_view(),name='topic-add'),
    #/questions/question/add/
    url(r'question/add/$',views.QuestionCreate.as_view(),name='question-add'),

    url(r'question/(?P<pk>[0-9]+)/$',views.QuestionUpdate.as_view(),name='question-update'),

    url(r'question/(?P<pk>[0-9]+)/delete/$',views.QuestionDelete.as_view(),name='question-delete'),

]
