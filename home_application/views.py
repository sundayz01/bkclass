# -*- coding: utf-8 -*-
import json
import re

from django.http import HttpResponse
from django.shortcuts import render

#from home_application.models import HostModel
from my_common.utils import render_json


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    return render(request, 'home_application/home.html')


def hellosunday(request):
    """
    首页
    """
    return render(request, 'home_application/hellosunday.html')

def helloblueking(request):
    """
    hellobuleking
    """
    return render(request, 'home_application/helloblueking.html')

# def say_hello(request):
#     data = request.POST.get('input',None)
#     data = 'Congratulations!' if data == 'Hello Blueking' else 'Try input Hello Blueking'
#     res = {'data': data}
#     return render_json(res)

def say_hello(request):
    """
    作业二后端逻辑验证
    """
    data = request.POST.get('input', None)
    data = 'Congratulations!' if data == 'Hello Blueking' else 'Try input Hello Blueking'
    res = {'data': data}
    return render_json(res)


