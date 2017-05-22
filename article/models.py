from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 100)# the title of blog
    category = models.CharField(max_length = 50, blank = True) # the tag of blog
    date_time = models.DateTimeField(auto_now_add = True) #the date of blog
    content = models.TextField(blank = True, null = True) #the content of blog
    
    #python3 use the __str__
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time'] # decreasing order 
