# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.views.decorators import csrf 
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from WebPostShow.models import station_info
import json
import os


# 接收POST请求数据
@csrf_exempt
def Labview_Post(request):
    ctx ={}
    if request.POST:
        a=(station_info.objects.get(station_name=request.POST['name']) )
        state=a.station_state.split(',')
        state[int(request.POST['serial'])-1]=request.POST['state']
        a.station_state=""
        for i in range(1,len(state)):
            if request.POST['state']=='9' :
                state[i-1]='9'
            if request.POST['state']=='0' and request.POST['serial']=='1' :
                state[i-1]='0'
            a.station_state = a.station_state + state[i-1] + ","
            ctx[str(i)+"i"]="{{"+str(i)+"i|safe|default:\""+state[i-1]+".jpg\" }}"
        a.save()
        static_html = request.POST['name']+"_static.html"
        content = render_to_string(static_html, ctx)
        static_file = open("WebPostShow/"+static_html, 'w')
        static_file.write(str(content.encode('utf-8') ))
        static_file.close()
    return render(request, "empty_static.html", ctx)

#返回GET请求值
@csrf_exempt
def Web_Get(request):
    ctx ={}
    if request.GET:
        a=(station_info.objects.get(station_name=request.POST['name']) )
        state=a.station_state.split(',')
    return state

