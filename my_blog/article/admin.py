from django.contrib import admin
# 导入models中新建的类
from .models import ArticlePost

# Register your models here.
admin.site.register(ArticlePost)
