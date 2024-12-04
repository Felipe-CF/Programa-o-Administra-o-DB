from rest_framework import serializers
from biblioteca.api.models.autor import Autor
from biblioteca.api.models.livro import Livro
from biblioteca.api.models.editora import Editora
from biblioteca.api.models.emprestimo import Emprestimo
from biblioteca.api.models.usuario import Usuario
from biblioteca.api.models.reserva import Reserva


class AutorSerializer(serializers.Serializer):
    class Meta:
        model = Autor
        fields = "__all__"


class UsuarioSerializer(serializers.Serializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class EmprestimoSerializer(serializers.Serializer):
    class Meta:
        model = Emprestimo
        fields = "__all__"


class EditoraSerializer(serializers.Serializer):
    class Meta:
        model = Editora
        fields = "__all__"


class LivroSerializer(serializers.Serializer):
    class Meta:
        model = Livro
        fields = "__all__"


class ReservaSerializer(serializers.Serializer):
    class Meta:
        model = Reserva
        fields = "__all__"
    