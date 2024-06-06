from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
