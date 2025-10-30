from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Empresa(models.Model):

    # Relacionamento 1 - 1 com usuário
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # Dados da Empresa
    nome = models.CharField(max_length=100, verbose_name="Nome da Empresa")
    cnpj = models.CharField(max_length=20, verbose_name="CNPJ")
    telefone = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)

    # Datas de criacao e atualização
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
