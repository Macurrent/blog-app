'''This is where i will define all my database'''
from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    '''creating table post with attribute title, author and body'''
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        '''change the title to a readable format, without this function, it will display post object(1)'''
        return self.title

    def get_absolute_url(self):  # new
        '''This function has been created due to the form that allows users to input data. 
        This will direct users to post_detail when there inputs are accepted'''
        return reverse('post_detail', args=[str(self.id)])
