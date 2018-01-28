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

    def get_passport(self, username, pwd=None):
        try:
            if pwd:
                obj = self.model.objects.get(username=username, password=pwd)
            else:
                obj = self.model.objects.get(username=username)
        except self.model.DoesNotExist:
            obj = None
        return obj


class Passport(BaseModel):
    objects = UserManage()
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField(max_length=20, verbose_name='邮箱')

    class Meta:
        db_table = 's_user_account'


class AddrManage(models.Manager):
    def get_address(self, passport_id):
        '''查询用户有没有默认地址'''
        try:
            addr = self.get(passport_id=passport_id, is_default=True)
        except self.model.DoesNotExist:
            addr = None
        return addr

    def add_info(self, passport_id, name, addr, zip_code, phone):
        if not self.get_address(passport_id):
            model = self.model(passport_id=passport_id, recipient_addr=addr,
                               recipient_name=name, recipient_phone=phone,
                               zip_code=zip_code, is_default=True)
        else:
            model = self.model(passport_id=passport_id, recipient_addr=addr,
                               recipient_name=name, recipient_phone=phone,
                               zip_code=zip_code)
        model.save()
        return model


class Address(BaseModel):
    objects = AddrManage()
    passport = models.ForeignKey('Passport', verbose_name='所属账户')
    recipient_name = models.CharField(max_length=24, verbose_name='收件人')
    recipient_addr = models.CharField(max_length=256, verbose_name='收件地址')
    recipient_phone = models.CharField(max_length=11, verbose_name='联系电话')
    zip_code = models.CharField(max_length=6, verbose_name='邮政编码')
    is_default = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        db_table = 's_user_address'
