from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title if len(self.title) < 30 else self.title[:30] + ' ...'