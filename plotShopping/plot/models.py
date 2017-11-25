#coding:utf-8
from django.db import models

# Create your models here.
class Age(models.Model):
    labels = models.CharField(max_length=100, unique=True, verbose_name='标签')
    data  = models.IntegerField(default=0, verbose_name='数据')


class Gender(models.Model):
    labels = models.CharField(max_length=100, unique=True, verbose_name='性别')
    data  = models.IntegerField(default=0, verbose_name='数据')


class Operate(models.Model):
    month=models.CharField(max_length=100, unique=True, verbose_name='月份',default='')
    click = models.IntegerField(default=0, verbose_name='点击量')
    addCart  = models.IntegerField(default=0, verbose_name='加入购物车的量')
    buy= models.IntegerField(default=0, verbose_name='购买量')
    collect = models.IntegerField(default=0, verbose_name='收藏量')