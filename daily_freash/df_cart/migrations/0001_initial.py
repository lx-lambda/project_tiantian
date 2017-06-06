# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
        ('df_goods', '0002_auto_20170603_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ccount', models.IntegerField(default=0)),
                ('cgood', models.ForeignKey(to='df_goods.GoodsInfo')),
                ('cuser', models.ForeignKey(to='df_user.UserInfo')),
            ],
        ),
    ]
