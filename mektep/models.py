from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Post(models.Model):

    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    data = models.DateTimeField()

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    pass
