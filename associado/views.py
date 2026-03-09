from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # O Django buscará automaticamente dentro da pasta templates/
    return render(request,'associado/index.html')

