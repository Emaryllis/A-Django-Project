import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')
django.setup()

import random
from faker import Faker
from DjangoApp.models import AccessRecord, Topic, Webpage

# Fake data algorithm

faker = Faker()
topics = ['Search', 'Social', 'Twitter', 'Facebook', ]

def addTopic():
    randomTopicName = random.choice(topics)
    randomTopic, created = Topic.objects.get_or_create(topicName=randomTopicName)
    if created: randomTopic.save()
    return randomTopic

def populateData(rowsToPopulate=5):
    for entry in range(rowsToPopulate):
        # Populate Webpages & AccessRecords
        fakeWebpage = Webpage.objects.get_or_create(topicName=addTopic(), siteName=faker.company(), url=faker.url())[0]
        accessRecord = AccessRecord.objects.get_or_create(userName=fakeWebpage, dateAccessed=faker.date())[0]
        fakeWebpage.save()
        accessRecord.save()

if __name__ == '__main__':
    print('Populating script!')
    populateData(20)
    print('Populating complete!')
