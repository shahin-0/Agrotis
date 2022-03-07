from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    pass

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    image = models.ImageField(null=False, blank=False, upload_to='images/', default='null')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('blog:post', args=(str(self.id)))
