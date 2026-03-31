from django.db import models


class Associado(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    ativo = models.BooleanField(default=True, null=False, blank=False)
    # chave estrangeira da empresa
    empresa = models.ForeignKey(
        'Empresa', on_delete=models.CASCADE, null=False, blank=False)
    # chave estrangeira do endereço
    endereco = models.ForeignKey(
        'Endereco', on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return self.nome+" - Ativo: " + str(self.ativo)

    # definir o nome da tabela
    class Meta:
        db_table = 'associado'


class Empresa(models.Model):
    orgao = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    ativo = models.BooleanField(default=True, null=False, blank=False)
    # nome do contato do orgão
    nome_contato = models.CharField(max_length=100, null=False, blank=False)
    # chave estrangeira do endereço
    endereco = models.ForeignKey(
        'Endereco', on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return self.nome+" - CNPJ: " + self.cnpj
    # definir o nome da tabela

    class Meta:
        db_table = 'empresa'


class Endereco(models.Model):
    # Baseado nos campos do wireframe
    logradouro = models.CharField("Endereço", max_length=255)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField("UF", max_length=2)
    cep = models.CharField("CEP", max_length=9)

    class Meta:
        db_table = 'endereco'
        verbose_name = 'Endereço'

    def __str__(self):
        return f"{self.logradouro}, {self.bairro} - {self.cidade}/{self.uf}"
