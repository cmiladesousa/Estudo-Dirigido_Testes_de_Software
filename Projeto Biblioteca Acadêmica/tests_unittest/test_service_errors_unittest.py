import unittest
from app_biblioteca.repository import InMemoryLivroRepository
from app_biblioteca.service import BibliotecaService, LivroInvalidoError


class TestBibliotecaServiceErros(unittest.TestCase):
    def test_titulo_vazio_deve_falhar(self):
        repo = InMemoryLivroRepository()
        service = BibliotecaService(repo)

        with self.assertRaises(LivroInvalidoError) as ctx:
            service.cadastrar_livro("1234567890", "   ", 2)

        self.assertIn("título obrigatório", str(ctx.exception).casefold())


if __name__ == "__main__":
    unittest.main()