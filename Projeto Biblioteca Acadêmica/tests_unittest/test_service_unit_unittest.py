import unittest
from unittest.mock import Mock
from app_biblioteca.service import BibliotecaService


class TestBibliotecaServiceComMock(unittest.TestCase):
    def test_cadastrar_livro_salva_no_repositorio(self):
        # Arrange
        repo = Mock()
        repo.buscar_por_isbn.return_value = None
        service = BibliotecaService(repo)

        # Act
        livro = service.cadastrar_livro(
            "1234567890",
            " Livro  Novo ",
            1,
        )

        # Assert
        self.assertEqual(livro.titulo, "Livro Novo")
        repo.salvar.assert_called_once()


if __name__ == "__main__":
    unittest.main()