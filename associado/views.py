from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # O Django buscará automaticamente dentro da pasta templates/
    return render(request,'associado/index.html')
# Função para carregar o perfil do associado
def perfil(request):
    return render(request, 'associado/perfil.html')
def beneficios(request):
    # Por enquanto, apenas renderizamos o HTML de design
    return render(request, 'associado/beneficios.html')
def carteirinha(request):
    # Aqui passamos o contexto 'vibe pwa' para o template
    return render(request, 'associado/carteirinha.html')
