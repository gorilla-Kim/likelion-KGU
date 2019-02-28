from django.db import models
from likelion.models import likelion

# Create your models here.

class Team(models.Model):
    likelions = models.ForeignKey(likelion, on_delete= models.CASCADE)
    name = models.CharField(max_length=20, default="이름")
    leader = models.BooleanField(default=False)
    operator = models.BooleanField(default=False)
    document = models.ImageField(upload_to='%Y/%m/%d/orig', blank=True)
    discription = models.TextField()