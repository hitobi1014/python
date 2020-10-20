from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("테스트세트트트")

def index2(request):
    return render(request,'index.html')