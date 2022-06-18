from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
User=get_user_model()
class Post(models.Model):
    
    Title = models.CharField(max_length = 200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
python manage.py makemigrations post