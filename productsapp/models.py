from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    post_description = models.CharField(max_length=500, blank=True)
    post_image = models.ImageField(blank=True, default="", upload_to="post_images/")
    body = models.TextField(default="")
    publish_date = models.DateTimeField(blank=True, default=timezone.now)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey('Post', related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=300, default="")
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)





