# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,verbose_name='标题')
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish = models.ForeignKey(to = "Publish",on_delete=models.CASCADE)#级联删除
    authors = models.ManyToManyField(to="Author")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "书籍"
        verbose_name_plural = verbose_name



class Publish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "出版设"
        verbose_name_plural = verbose_name

class Author(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.CharField(max_length=32)
    # ad = models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "作者"
        verbose_name_plural = verbose_name

class AuthorDetail(models.Model):
    addr = models.CharField(max_length=32)
    tel = models.IntegerField()
    class Meta:
        verbose_name = "作者详情"
        verbose_name_plural = verbose_name
#
# class Author2Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     book = models.ForeignKey("Book",on_delete=models.CASCADE)
#     author = models.ForeignKey("Author",on_delete=models.CA

class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    dep = models.CharField(max_length=32)
    pro = models.CharField(max_length=32)
    salary = models.DecimalField(max_digits=8,decimal_places=2)

