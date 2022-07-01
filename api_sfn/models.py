from django.db import models
import datetime

class Article(models.Model):
    site_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=2048)
    imageUrl = models.URLField(default='github.com/luizAdamchuk.png',max_length=2048)
    url = models.URLField(default='github.com/luizAdamchuk',max_length=2048)
    newsSite = models.CharField(max_length=2048)
    summary = models.CharField(max_length=2048)
    publishedAt = models.DateField(("publishedAt"), default=datetime.date.today)
    updatedAt = models.DateField(("updatedAt"), default=datetime.date.today)
    featured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

class CronJob(models.Model):
    quantity = models.IntegerField()
    runAt = models.DateField(("runAt"), default=datetime.date.today)
    
    def __str__(self) -> str:
        return "{quantity} - {runAt}".format(quantity=self.quantity,runAt=self.runAt)
