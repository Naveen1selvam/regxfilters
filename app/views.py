from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Topic is Inserted')
        else:
            return HttpResponse('data is not valid')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WF=WebpageForm()
    d={'WF':WF}
    if request.method=='POST':
        WFD=WebpageForm(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse('Webpage is inserted')
        else:
            return HttpResponse('Data is not valid')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    AF=AccessForm()
    d={'AF':AF}
    if request.method=='POST':
        AFD=AccessForm(request.POST)
        if AFD.is_valid():
            AFD.save()
            return HttpResponse('Access is inserted')
        else:
            return HttpResponse('Data is not valid')
    return render(request,'insert_access.html',d)