from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to ='images/')
    icon = models.ImageField(upload_to ='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    # this function for db to use title as name of the record.
    def __str__(self):
        return self.title

    def summary(self):
        briefText = self.body
        if(len(self.body) > 100):
            briefText = self.body[:100] + '...'
        return briefText

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

   
    
