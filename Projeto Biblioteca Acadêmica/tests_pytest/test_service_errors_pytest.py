import pytest
from app_biblioteca.repository import InMemoryLivroRepository
from app_biblioteca.service import (
    BibliotecaService, LivroInvalidoError, LivroDuplicadoError,
)


def criar_service():
    return BibliotecaService(InMemoryLivroRepository())


def test_isbn_com_letras_deve_falhar():
    service = criar_service()
    with pytest.raises(LivroInvalidoError) as ctx:
        service.cadastrar_livro("abcdefghij", "Livro", 2)
    assert "isbn inválido" in str(ctx.value).casefold()


def test_titulo_vazio_deve_falhar():
    service = criar_service()
    with pytest.raises(LivroInvalidoError) as ctx:
        service.cadastrar_livro("1234567890", "   ", 2)
    assert "título obrigatório" in str(ctx.value).casefold()


def test_zero_exemplares_deve_falhar():
    service = criar_service()
    with pytest.raises(LivroInvalidoError) as ctx:
        service.cadastrar_livro("1234567890", "Livro", 0)
    assert "exemplares" in str(ctx.value).casefold()


def test_livro_duplicado_deve_falhar():
    service = criar_service()
    service.cadastrar_livro("1234567890", "Livro", 2)
    with pytest.raises(LivroDuplicadoError) as ctx:
        service.cadastrar_livro("1234567890", "Outro título", 2)
    assert "já cadastrado" in str(ctx.value).casefold()
