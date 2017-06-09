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
            name='DetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('ocount', models.IntegerField()),
                ('ogood', models.ForeignKey(to='df_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('odata', models.DateField(auto_now_add=True)),
                ('oispay', models.BooleanField(default=False)),
                ('ototal', models.DecimalField(max_digits=6, decimal_places=2)),
                ('oaddr', models.CharField(max_length=150)),
                ('ouser', models.ForeignKey(to='df_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='detailinfo',
            name='order',
            field=models.ForeignKey(to='df_order.OrderInfo'),
        ),
    ]
