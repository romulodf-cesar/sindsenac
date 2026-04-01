from django.contrib import admin

from associado.models import Associado, Empresa, Endereco

# admin.site.register(Associado)
admin.site.register(Empresa)
admin.site.register(Endereco)


class EnderecoInline(admin.StackedInline):
    model = Endereco
    extra = 1
    # Isso remove o campo 'empresa' de dentro da caixa azul de endereço
    exclude = ['empresa']
    fields = ('logradouro', 'bairro', 'cidade', 'uf', 'cep')


@admin.register(Associado)
class AssociadoAdmin(admin.ModelAdmin):
    inlines = [EnderecoInline]
