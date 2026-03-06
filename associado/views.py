from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>SindApp</h1><p>Bem-vindo ao portal do associado!</p>')