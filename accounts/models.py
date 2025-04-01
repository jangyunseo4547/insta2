from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.

# 유저
class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500,500],
        crop=['middle', 'center'],
        upload_to='profile'
    )
# symmetrical=False : 비대칭구조 (1-> 2 팔로우 / 2 ->1 팔로우는 다르기 때문)
    followings = models.ManyToManyField(
        'self', 
        related_name='followers',
        symmetrical=False
    )

