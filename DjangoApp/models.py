from django.contrib.auth.models import User
from django.db import models

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

class UserProfileInfo(models.Model):
    # Extending from django.contrib.auth.models.User model to add our own attributes
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add the additional attributes here
    portfolioSite = models.URLField(blank=True)
    profilePic = models.ImageField(upload_to='profilePics', blank=True)

    def __str__(self):
        return self.user.username
