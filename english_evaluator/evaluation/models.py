from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Question(models.Model):
    QUESTION_TYPES = [
        ('reading', 'Reading'),
        ('listening', 'Listening'),
    ]
    type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    question = models.TextField()
    options = models.JSONField()  # Store options as a list of strings
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question
