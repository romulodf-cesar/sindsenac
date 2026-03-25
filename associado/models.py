from django.db import models

# Create your models here.


class Associado(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    ativo = models.BooleanField(default=True, null=False, blank=False)
    # chave estrangeira da empresa
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=False, blank=False)
    def __str__(self):
        return self.nome+" - Ativo: " + str(self.ativo)
    
    # definir o nome da tabela
    class Meta:
        db_table = 'associado'
    
class Empresa(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    
    def __str__(self):
        return self.nome+" - CNPJ: " + self.cnpj
    # definir o nome da tabela
    class Meta:
        db_table = 'empresa'
