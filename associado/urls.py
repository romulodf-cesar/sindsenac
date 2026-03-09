from django.urls import path
from associado.views import index,perfil

urlpatterns = [
   path('',index,name='index'),
   path('perfil/', perfil, name='perfil'), # Rota amigável: /perfil/
]