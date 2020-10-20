from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=300, default="")
    product_image = models.ImageField(blank=True, default="", upload_to="product_images/")
    product_description = models.TextField(default="")
    publish_date = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.product_name

class ProductComments(models.Model):
    post = models.ForeignKey('Product', related_name="productcomments", on_delete=models.CASCADE)
    name = models.CharField(max_length=300, default="")
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name
