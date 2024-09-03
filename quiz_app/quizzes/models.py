from django.db import models
from django.contrib.auth.models import AbstractUser

class StudentUser(AbstractUser): 
    username = models.CharField(max_length=150, unique=True)

    def save(self, *args, **kwargs): 
        self.username = self.username.lower() 
        super(StudentUser, self).save(*args, **kwargs) 

class Category(models.Model): 
    name = models.CharField(max_length=100)

    def __str__(self): 
        return self.name 
    
class Question(models.Model): 
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  # This field links to the Category model
    text = models.TextField()
    choices = models.JSONField()  # Store choices as a JSON object
    correct_answers = models.JSONField()  # Store correct answers as a JSON object

    def __str__(self):
        return self.text
