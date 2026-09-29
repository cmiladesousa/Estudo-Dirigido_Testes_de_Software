from dataclasses import dataclass


class LivroInvalidoError(ValueError):
    pass


class LivroDuplicadoError(ValueError):
    pass


@dataclass
class Livro:
    isbn: str
    titulo: str
    exemplares: int