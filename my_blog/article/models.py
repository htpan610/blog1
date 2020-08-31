from django.db import models
# 引入User
from django.contrib.auth.models import User
# 引入处理时间的相关事物
from django.utils import timezone


# Create your models here.
# The class is inherited from models.Model
class ArticlePost(models.Model):
    # foreignkey means many to one,
    # on_delete means when you del User the author will also be del
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(auto_now=True)

    # 定义内部类,meta类用于定义某些属性,ordering是元祖,即内部内容不可更改,不要忘记逗号
    class Meta:
        ordering = ('-created_time',)

    # __str__ 当调用整个class类时的返回值
    def __str__(self):
        return self.title
