from django.db import models

# Create your models here.
class likelion(models.Model):
    group_number = models.IntegerField(blank=False)
    programming_lang = models.CharField(max_length=125,default="no language")

    def __str__(self):
        return "{}기수".format(self.group_number)