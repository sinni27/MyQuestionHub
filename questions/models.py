from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=300)
    related_to = models.CharField(max_length=300)

    def __str__(self):
        return self.topic_name

class Question(models.Model):
    posted_by = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
