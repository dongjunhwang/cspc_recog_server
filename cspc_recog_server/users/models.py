from django.db import models
from django.contrib.auth.models import User
import datetime

def profileImageUpload(instance, filename):
    return 'image/profile/{0}/{1}'.format(instance.id,filename)


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    #group_admin_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    group_admin_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name


class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=100)
    last_visit_time = models.DateTimeField(auto_now=True)  # 저장시 자동 시간 업데이트
    visit_time_sum = models.DurationField(default=datetime.timedelta())
    is_online = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to = profileImageUpload,blank=True)

    def __str__(self):
        return self.nick_name
