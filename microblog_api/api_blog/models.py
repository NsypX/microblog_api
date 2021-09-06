from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    likes = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return("Title- " + self.title + "\nBody- " +  self.body + "\nLikes- " + str(self.likes) + "\nDate- " + str(self.date))


