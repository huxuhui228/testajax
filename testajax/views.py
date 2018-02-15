from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.
def index(request):
    val = os.popen("ps -ef").read()
    if request.is_ajax():
        return render(request,'testajax/main.html', {'val':val})
    return render(request,'testajax/index.html', {'val':val})