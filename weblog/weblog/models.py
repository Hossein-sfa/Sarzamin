from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    
    def __str__(self):
        return self.title

