from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
choice  = (
	('teacher', 'Teacher'),
	('student', 'Student')
	)
class User(AbstractUser):
	role = models.CharField(max_length=100, choices = choice, default="")