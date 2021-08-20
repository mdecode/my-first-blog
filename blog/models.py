from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
# this class is for post type, to have info about the posts in blog
# models.Model means Post is a django model, so Django knows that it should be saved in db
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
