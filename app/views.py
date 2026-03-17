from urllib import request

from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def outraPagina(request):
    return render(request,'app/outraPagina.html')
