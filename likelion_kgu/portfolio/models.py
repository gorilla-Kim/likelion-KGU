from django.db import models
from likelion.models import likelion
# Create your models here.
class Portfolio(models.Model):
    likelion = models.ForeignKey(likelion, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/', null=True)
    title = models.CharField(max_length=125, default="제목을 입력해주세요.")
    description = models.TextField(default="설명을 입력해 주세요.")
    git_link = models.CharField(max_length=125, blank=True, null=True)
    blog_link = models.CharField(max_length=125, blank=True, null=True)

    def delete(self, *args, **kwargs):
        self.document.delete()
        super(portfolio, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:20]