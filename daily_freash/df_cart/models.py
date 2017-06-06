from django.db import models
from df_user.models import UserInfo
from df_goods.models import GoodsInfo

# Create your models here.
class MyCart(models.Model):
    cuser = models.ForeignKey(UserInfo)
    cgood = models.ForeignKey(GoodsInfo)
    ccount = models.IntegerField(default=0)
