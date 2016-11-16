from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        pass
    def popular(self):
        pass
  
  
class Question(models.Model):

  objects=QuestionManager()
  title=models.CharField(max_length=255,null=True)
  text=models.TextField(null=True)
  added_at=models.DateField(null=True)
  rating=models.IntegerField(null=True)
  author=models.ForeignKey(User, related_name='author1_id')
  likes=models.ManyToManyField(User,related_name='likes1_id')

  
class Answer(models.Model):
  text=models.TextField(null=True)
  added_at=models.DateField(null=True)
  question=models.CharField(max_length=255,null=True)
  author=models.ForeignKey(User)

  
