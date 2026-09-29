from .domain import Livro, LivroDuplicadoError, LivroInvalidoError
from .validators import normalizar_titulo, validar_isbn10


class BibliotecaService:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def cadastrar_livro(self, isbn, titulo, exemplares):
        if not validar_isbn10(isbn):
            raise LivroInvalidoError("ISBN inválido")

        titulo_normalizado = normalizar_titulo(titulo)
        if not titulo_normalizado:
            raise LivroInvalidoError("Título obrigatório")

        if exemplares <= 0:
            raise LivroInvalidoError("Exemplares deve ser > 0")

        if self.repositorio.buscar_por_isbn(isbn) is not None:
            raise LivroDuplicadoError("Livro já cadastrado")

        livro = Livro(
            isbn=isbn,
            titulo=titulo_normalizado,
            exemplares=exemplares,
        )
        self.repositorio.salvar(livro)
        return livro