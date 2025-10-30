from django.contrib import admin
from .models import Empresa


# Register your models here.
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'telefone', 'email', 'data_criacao']
    list_filter = ['data_criacao']
    search_fields = ['nome', 'cnpj']