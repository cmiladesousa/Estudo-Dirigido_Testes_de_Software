from app_biblioteca.repository import InMemoryLivroRepository
from app_biblioteca.service import BibliotecaService


def test_cadastrar_livro_valido_salva_no_repositorio():
    # Arrange
    repo = InMemoryLivroRepository()
    service = BibliotecaService(repo)

    # Act
    livro = service.cadastrar_livro(
        "1234567890",
        " Testes   Python ",
        2,
    )

    # Assert
    assert livro.titulo == "Testes Python"
    assert repo.buscar_por_isbn("1234567890").exemplares == 2