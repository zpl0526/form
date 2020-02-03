# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models
from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','price')


class EmpAdmin(admin.ModelAdmin):
    list_display = ('salary','age','name','pro')
    list_editable = ('name','age','pro')
admin.site.register(models.User)
admin.site.register(models.Book,BookAdmin)
admin.site.register(models.Author)
admin.site.register(models.Publish)
admin.site.register(models.Emp,EmpAdmin)
# Register your models here.
