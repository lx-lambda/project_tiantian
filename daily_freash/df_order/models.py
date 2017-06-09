# coding=utf-8
from django.db import models

# Create your models here.
class OrderInfo(models.Model):
    oid = models.CharField(max_length=20,primary_key=True) # 时间+用户编号
    ouser = models.ForeignKey('df_user.UserInfo')
    odata = models.DateField(auto_now_add=True)
    oispay = models.BooleanField(default=False)
    ototal = models.DecimalField(max_digits=6,decimal_places=2)
    oaddr = models.CharField(max_length=150)


class DetailInfo(models.Model):
    order = models.ForeignKey(OrderInfo)
    ogood = models.ForeignKey('df_goods.GoodsInfo')
    oprice = models.DecimalField(max_digits=5,decimal_places=2)
    ocount = models.IntegerField()
