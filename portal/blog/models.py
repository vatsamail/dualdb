from django.db import models

class Content(models.Model):
    title       = models.CharField(max_length=100)
    blog        = models.TextField()
    image       = models.FilePathField(path="static/img", null=True, blank=True)
    

    def __str__(self):
        return self.title


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
