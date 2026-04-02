# admin.py

from django.contrib import admin
from django.utils.html import format_html, mark_safe
from .models import EnderecoAssociado, EnderecoEmpresa, Empresa, Associado


# ─────────────────────────────────────────
#  MODELOS DE ENDEREÇO (Opção 1 — separados)
#  Certifique-se de ter esses modelos em models.py
# ─────────────────────────────────────────

# Se ainda não criou, adicione ao models.py:
#
# class EnderecoEmpresa(models.Model):
#     empresa    = models.OneToOneField(Empresa, on_delete=models.CASCADE, related_name="endereco")
#     logradouro = models.CharField(max_length=255)
#     bairro     = models.CharField(max_length=100)
#     cidade     = models.CharField(max_length=100)
#     uf         = models.CharField(max_length=2)
#     cep        = models.CharField(max_length=9)
#     class Meta:
#         db_table = 'endereco_empresa'
#
# class EnderecoAssociado(models.Model):
#     associado  = models.OneToOneField(Associado, on_delete=models.CASCADE, related_name="endereco")
#     logradouro = models.CharField(max_length=255)
#     bairro     = models.CharField(max_length=100)
#     cidade     = models.CharField(max_length=100)
#     uf         = models.CharField(max_length=2)
#     cep        = models.CharField(max_length=9)
#     class Meta:
#         db_table = 'endereco_associado'


# ══════════════════════════════════════════
#  INLINES
# ══════════════════════════════════════════

class EnderecoEmpresaInline(admin.StackedInline):
    model = EnderecoEmpresa
    can_delete = False          # Endereço não existe sem empresa
    verbose_name = "Endereço"
    verbose_name_plural = "Endereço da Empresa"
    min_num = 1              # Obriga ao menos 1 endereço
    max_num = 1              # Garante o 1:1 no formulário
    extra = 1
    fields = ("logradouro", "bairro", "cidade", "uf", "cep")


class EnderecoAssociadoInline(admin.StackedInline):
    model = EnderecoAssociado
    can_delete = False
    verbose_name = "Endereço"
    verbose_name_plural = "Endereço do Associado"
    min_num = 1
    max_num = 1
    extra = 1
    fields = ("logradouro", "bairro", "cidade", "uf", "cep")


# ══════════════════════════════════════════
#  ADMIN — EMPRESA
# ══════════════════════════════════════════

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    inlines = [EnderecoEmpresaInline]

    list_display = ("orgao", "cnpj", "nome_contato", "status_badge")
    list_filter = ("ativo",)
    search_fields = ("orgao", "cnpj", "nome_contato")
    ordering = ("orgao",)

    fieldsets = (
        ("Dados da Empresa", {
            "fields": ("orgao", "cnpj", "nome_contato", "ativo")
        }),
    )

    @admin.display(description="Status")
    def status_badge(self, obj):
        if obj.ativo:
            return format_html(
                '<span style="color:green; font-weight:bold;">● Ativo</span>'
            )
        return format_html(
            '<span style="color:red; font-weight:bold;">● Inativo</span>'
        )


# ══════════════════════════════════════════
#  ADMIN — ASSOCIADO
# ══════════════════════════════════════════

@admin.register(Associado)
class AssociadoAdmin(admin.ModelAdmin):
    inlines = [EnderecoAssociadoInline]

    list_display = ("nome", "cpf", "email", "empresa", "status_badge")
    list_filter = ("ativo", "empresa")
    search_fields = ("nome", "cpf", "email")
    ordering = ("nome",)
    # Empresa precisa ter search_fields definido ✅
    autocomplete_fields = ("empresa",)

    fieldsets = (
        ("Dados Pessoais", {
            "fields": ("nome", "cpf", "email", "ativo")
        }),
        ("Vínculo", {
            "fields": ("empresa",)
        }),
    )

    # ✅ Forma correta — use format_html COM placeholder, ou mark_safe para string fixa


    @admin.display(description="Status")
    def status_badge(self, obj):
       if obj.ativo:
         return format_html(
            '<span style="color:{}; font-weight:bold;">● {}</span>',
            "green", "Ativo"
         )
       return format_html(
           '<span style="color:{}; font-weight:bold;">● {}</span>',
           "red", "Inativo"
       )
