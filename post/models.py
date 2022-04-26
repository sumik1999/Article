from django.db import models
from user.models import User
# Create your models here.
class Post(models.Model):

    title = models.CharField(blank=False,null=False,max_length=255)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
