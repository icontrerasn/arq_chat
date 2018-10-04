from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=200)
    ip = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date posted')

