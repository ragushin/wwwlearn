from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):                                          
  def new():                                                              
    pass                                                            
  def popular():                                                          
    pass 

class Question(models.Model):
  objects = QuestionManager() 
  
  title=models.CharField(max_length=255)
  text=models.TextField()
  added_at=models.DateField()
  rating=models.IntegerField()
  author=models.ForeignKey(User, related_name='author1_id')
  likes=models.ManyToManyField(User,related_name='likes1_id')

  
class Answer(models.Model):
  text=models.TextField()
  added_at=models.DateField()
  question=models.CharField(max_length=255)
  author=models.ForeignKey(User)

  
class QuestionManager(models.Manager):                                          
  def new():                                                              
    pass                                                            
  def popular():                                                          
    pass 
