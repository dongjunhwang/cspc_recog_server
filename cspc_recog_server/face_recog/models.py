from users.models import Profile
from django.db.models.deletion import CASCADE
from django.db import models


class Face(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image_base64 = models.TextField()

    def __str__(self):
        return self.profile.user_id.username
# Create your models here.
