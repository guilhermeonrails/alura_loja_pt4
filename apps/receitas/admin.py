from django.contrib import admin
from receitas.models.receita import Receita
from receitas.models.pedir_receita import PedirReceita

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 5

class PedidosDeReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita','categoria', 'pessoa','date_receita', 'pedido_atendido')
    list_display_links = ('id', 'nome_receita')
    list_editable = ('pedido_atendido',)
    list_filter = ('pedido_atendido',)
    list_per_page = 25

admin.site.register(Receita, ListandoReceitas)
admin.site.register(PedirReceita, PedidosDeReceitas)