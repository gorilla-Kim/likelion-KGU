from django.db import models
from likelion.models import likelion
# Create your models here.
class portfolio(models.Model):
    likelion = models.ForeignKey(likelion, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/', null=True)
    description = models.TextField(default="설명을 입력해 주세요.")
    git_link = models.CharField(max_length=125, blank=True, null=True)
    blog_link = models.CharField(max_length=125, blank=True, null=True)

    def delete(self, *args, **kwargs):
        self.document.delete()
        super(document, self).delete(*args, **kwargs)