from django.db import models

# Create your models here.
class Topic(models.Model):
    topicName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.topicName

class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.site_name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.date.__str__()
