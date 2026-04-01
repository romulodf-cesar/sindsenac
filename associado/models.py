from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField("Logradouro", max_length=255)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField("UF", max_length=2)
    cep = models.CharField("CEP", max_length=9)
    # Em vez de Associado ter um Endereço, o Endereço pertence a um Associado
    associado = models.OneToOneField(
        'Associado', on_delete=models.CASCADE, null=True, blank=True)
    empresa = models.OneToOneField(
        'Empresa', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'endereco'
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return f"{self.logradouro}, {self.bairro} - {self.cidade}/{self.uf}"


class Empresa(models.Model):
    orgao = models.CharField("Órgão/Empresa", max_length=100)
    cnpj = models.CharField("CNPJ", max_length=14)
    ativo = models.BooleanField(default=True)
    nome_contato = models.CharField("Nome do Contato", max_length=100)

    class Meta:
        db_table = 'empresa'

    def __str__(self):
        return f"{self.orgao} - CNPJ: {self.cnpj}"


class Associado(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=14)
    ativo = models.BooleanField(default=True)

    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, related_name="associados"
    )

    class Meta:
        db_table = 'associado'

    def __str__(self):
        status = "Ativo" if self.ativo else "Inativo"
        return f"{self.nome} - {status}"
