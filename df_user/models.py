from django.db import models
from db.base_model import BaseModel
# Create your models here.

class UserManage(models.Manager):
    def add_user(self, name, pwd, email):
        user = self.model()
        user.username = name
        user.password = pwd
        user.email = email
        user.save()
        return user

class Passport(BaseModel):
    objects = UserManage()
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField(max_length=20, verbose_name='邮箱')

    class Meta:
        db_table = 's_user_account'