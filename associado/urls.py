from django.urls import path
from associado.views import index

urlpatterns = [
   path('',index,name='index')
]