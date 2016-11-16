from django.db import models
from django.contrib.auth.models import User

Class Question(models.Model):
  objects = QuestionManager() 
  
  title=models.CharField()
  text=models.TextField()
  added_at=models.DateField()
  rating=models.IntegerField()
  author=models.ForeignKey(User)
  likes=models.ManyToManyField(User)

  
Class Answer(models.Model):
  text=models.TextField()
  added_at=models.DateField()
  question=models.CharField()
  author=models.ForeignKey(User)
  
  
class QuestionManager(models.Manager):                                          
  def new():                                                              
    pass                                                            
  def popular():                                                          
    pass 
