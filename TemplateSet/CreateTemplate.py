# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.views.decorators import csrf 
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from WebPostShow.models import station_info
import json
import os

def Create_Single_Template(name,num,img_add):
    item_list=[]
    ctx={}
    tempstr=""
    for i in range(1,int(num)+1):
        item_list.append("{{"+str(i)+"i|safe|default:\"9.jpg\"}}")
        tempstr=tempstr+"9,"
    ctx['item_list']=item_list
    ctx['template_name']="{{"+name+"}}"
    ctx['img_add']=img_add    
    Single_Template = "WebPostShow/"+name+"_static.html"   
    content = render_to_string('GeneralTemplate.html', ctx)
    static_file = open(Single_Template, 'w')
    static_file.write(str(content.encode('utf-8') ))
    static_file.close()

    station_info.objects.create(station_name=name,station_state=tempstr)
    bb=station_info.objects.filter(station_name=name)
    bb.delete()
    station_info.objects.create(station_name=name,station_state=tempstr)

    return

# 接收POST请求数据
@csrf_exempt
def Template_Post(request):    
    if request.POST:
        Create_Single_Template(request.POST['name'],request.POST['num'],request.POST['img']);
    return render_to_response("post_template.html")
