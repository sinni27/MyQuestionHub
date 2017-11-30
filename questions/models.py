from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=300)
    related_to = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse('questions:topic_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.topic_name

class Question(models.Model):
    posted_by = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('questions:index')

    def __str__(self):
        return self.content
