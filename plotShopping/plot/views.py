#coding:utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from  plot.handle import getAge,getGender,getOperate


@csrf_exempt
def age(request):
    if request.method == 'POST':
        dic=getAge()
        dic=json.dumps(dic)
        return HttpResponse(json.dumps(dic))
    if request.method == 'GET':
        return render(request, 'age.html', locals())


@csrf_exempt
def gender(request):
    if request.method == 'POST':
        dic=getGender()
        dic=json.dumps(dic)
        return HttpResponse(json.dumps(dic))
    if request.method == 'GET':
        return render(request, 'gender.html', locals())

@csrf_exempt
def operate(request):
    if request.method == 'POST':
        dic=getOperate()
        dic=json.dumps(dic)
        return HttpResponse(json.dumps(dic))
    if request.method == 'GET':
        return render(request, 'operate.html', locals())