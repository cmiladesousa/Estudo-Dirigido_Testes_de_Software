def validar_isbn10(isbn: str) -> bool:
    if isbn is None:
        return False
    somente_digitos = isbn.replace("-", "")
    return (
        len(somente_digitos) == 10
        and somente_digitos.isdigit()
    )


def normalizar_titulo(titulo: str) -> str:
    if titulo is None:
        raise ValueError("título obrigatório")
    partes = titulo.strip().split()
    return " ".join(partes)