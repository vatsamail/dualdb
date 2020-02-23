from django.db import models

class Content(models.Model):
    title       = models.CharField(max_length=100)
    blog        = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    genres =  models.ManyToManyField('Genre', related_name='genre')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'nosql'

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'nosql'


#########################################################################

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='category')
    related_posts = models.ManyToManyField('Post')

    def __str__(self):
        return self.title
