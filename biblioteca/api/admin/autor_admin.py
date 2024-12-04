from django.contrib import admin
from biblioteca.api.models.autor import Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('Nome do Autor', 'Editora')

    search_fields = ('nome', 'editora__nome')

    list_filter = ('editora')

    ordering = ['nome']  