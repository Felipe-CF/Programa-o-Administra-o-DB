
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from biblioteca.api.views.autor_view import AutorView
from biblioteca.api.views.livro_view import LivroView
from biblioteca.api.views.usuario_view import UsuarioView
from biblioteca.api.views.editora_view import EditoraView
from biblioteca.api.views.reserva_view import ReservaView
from biblioteca.api.views.emprestimo_view import EmprestimoView


rotas = routers.DefaultRouter()
rotas.register(r'livro', LivroView)
rotas.register(r'autor', AutorView)
rotas.register(r'usuario', UsuarioView)
rotas.register(r'reserva', ReservaView)
rotas.register(r'editora', EditoraView)
rotas.register(r'emprestimo', EmprestimoView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rotas.urls))
]
