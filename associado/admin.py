from django.contrib import admin

from associado.models import Associado, Empresa, Endereco

admin.site.register(Associado)
admin.site.register(Empresa)
admin.site.register(Endereco)