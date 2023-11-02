from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField 
class Note(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    picture = CloudinaryField('image/', null=True, blank=True ,folder='user_images')
    def __str__(self):
        return self.title
