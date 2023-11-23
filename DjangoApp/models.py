from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Topic(models.Model):
    topicName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.topicName

class Webpage(models.Model):
    topicName = models.ForeignKey(Topic, on_delete=models.CASCADE)
    siteName = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.siteName

class AccessRecord(models.Model):
    userName = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    dateAccessed = models.DateField()

    def __str__(self):
        return self.dateAccessed.__str__()
