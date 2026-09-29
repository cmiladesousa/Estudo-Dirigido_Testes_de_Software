from typing import Optional
from .domain import Livro


class InMemoryLivroRepository:
    def __init__(self):
        self._livros: dict[str, Livro] = {}

    def buscar_por_isbn(self, isbn: str) -> Optional[Livro]:
        livro = self._livros.get(isbn)
        if livro is None:
            return None
        return Livro(livro.isbn, livro.titulo, livro.exemplares)

    def salvar(self, livro: Livro) -> None:
        self._livros[livro.isbn] = Livro(
            livro.isbn,
            livro.titulo,
            livro.exemplares,
        )