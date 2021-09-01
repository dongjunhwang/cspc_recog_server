from users.models import Profile
from django.db.models.deletion import CASCADE
from django.db import models
import json


class Face(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.profile.user_id.username

    def set_image(self, x):
        self.image = json.dumps(x)

    def get_image(self):
        return json.loads(self.image)
# Create your models here.
