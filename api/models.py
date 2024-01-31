from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserSession(models.Model):

    STATE_CHOICES = (
        ('greeting', 'Greeting'),
        ('question', 'Question'),
        ('answer', 'Answer'),
        ('end', 'End'),
    )
    session_id = models.CharField(max_length=255, unique=True)
    current_state = models.CharField(
        max_length=50, 
        choices=STATE_CHOICES, 
        default='greeting'
    )

class Step(models.Model):
    name = models.CharField(max_length=255)
    response_message = models.TextField()
    next_state = models.CharField(max_length=255, null=True, blank=True)

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)