# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import widgets
from django.shortcuts import render, HttpResponse, redirect
from app01.models import User


class UserForm(forms.Form):
    msg = {"required": "该字段不能为空"}
    username = forms.CharField(min_length=5,
                               error_messages=msg,
                               widget=widgets.TextInput(attrs={"class": "form-control"}),
                               label="用户名"
                               )
    pwd = forms.IntegerField(error_messages=msg,
                             widget=widgets.PasswordInput(attrs={"class": "form-control"}),
                             label="密码"
                             )
    email = forms.EmailField(error_messages={"invalid": "邮箱格式错误"},
                             widget=widgets.EmailInput(attrs={"class": "form-control"}),
                             label="邮箱"
                             )


def login(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            info = form.cleaned_data
            User.objects.create(**info)
            return HttpResponse('歡迎登錄')
        else:
            errors = form.errors
            print(errors)
            return render(request, 'login.html',locals())

    else:
        form = UserForm()  # 这是空的类　渲染出来的是空的input标签
        return render(request, 'login.html', {'form':form})


def abc(request):
    return HttpResponse('rion')

def xyz(request):
    return render(request, "xyz.html")
