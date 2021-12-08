from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField 
from django.utils import timezone 
from django.urls import reverse

from taggit.managers import TaggableManager


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publish')

class Post(models.Model):

    STATUS_CHOICES = [('draft', 'Draft'),
                      ('publish', 'Publish')]

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, 
                            unique_for_date='published')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25,
                              choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager() # The default manager.
    publish = PostManager() # The publish manager.

    tags = TaggableManager()

    class Meta:
        ordering = ('-published',)                     

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        # return reverse('blog:post_detail',kwargs={'post_id': self.id,'slug': self.slug})
        return reverse('blog:post_detail',args=[self.id, self.slug])
        

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, 
                            related_name='comments',
                            on_delete=models.CASCADE) 
    commented = models.DateTimeField(default=timezone.now)                                   