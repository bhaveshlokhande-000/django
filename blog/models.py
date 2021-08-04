from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse;

# create your model here

class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")
    
            
            #.filter(status='Published')
    options=(
        ("draft","Draft"),
        ("published","Published"),
    )

    #blogId = models.IntegerField(primary_key = True)
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    publish=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts') #username
    content=models.TextField()
    status=models.CharField(max_length=10,choices=options,default='draft')
    objects=models.Manager() #default manager
    new_manager=NewManager() #custom manager

    def get_absolute_urls(self):
        return reverse('blog:post_single',args=[self.id])

    class Meta:
        ordering= ('-publish',)


    def __str__(self):
        return self.title
    
    