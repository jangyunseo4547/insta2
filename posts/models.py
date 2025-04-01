from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = ResizedImageField(
        size = [500,500],
        crop = ['middle', 'center'],
        upload_to = 'image/%Y/%m',
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 좋아요를 누른 유저
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name = 'like_posts', #User와 Post를 M: N 연결
    )

class Comment(models.Model):
    content = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)