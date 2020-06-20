from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=12)
    register_date = models.DateTimeField(auto_now_add=True, null=True)  # 如果设置为自动设置时间，要添加可以为空，默认是不为空的
