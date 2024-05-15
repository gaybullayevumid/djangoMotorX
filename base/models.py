from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.FileField(upload_to="post-images")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title