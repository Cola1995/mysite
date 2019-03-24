from django.db import models


# Create your models here.
# ORM相关的类只能写在这个文件里，别的文件找不到


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)  # 创建主键字段id
    name = models.CharField(null=False, max_length=20)  # name字段不能为空
