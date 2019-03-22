from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length =13,blank=True)

    def __str__(self):
        return self.first_name
    class meta:
        ordering =['first_name']
    
    def save_editor(self):
        self.save()


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey('Editor', on_delete=models.PROTECT)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)