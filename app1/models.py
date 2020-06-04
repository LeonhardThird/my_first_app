from django.db import models

class Post(models.Model):
    content = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now=True)
    

    # def __str__(self):
    #     return self.content
