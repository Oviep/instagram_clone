from django.db import models


# Create your models here.
class Post(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
