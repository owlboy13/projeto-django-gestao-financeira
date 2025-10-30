from django.contrib import admin
from .models import Categoria, Transacao


# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'descricao']
    list_filter = ['nome', 'tipo']
    search_fields = ['nome']

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'valor', 'data', 'categoria', 'empresa']
    list_filter = ['data', 'categoria', 'empresa']
    search_fields = ['descricao']
    date_hierarchy = 'data'