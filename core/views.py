from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("""
        <h1>Bem-vindo ao Flow Finance! </h1>
        <p>Seu Sistema de Gestão Financeira</p>
        <a href='/admin/'>Acessar Admin</a>
    """
    )
