import pytest
from app_biblioteca.validators import (
    normalizar_titulo,
    validar_isbn10,
)


def test_validar_isbn10_aceita_10_digitos():
    assert validar_isbn10("1234567890") is True


@pytest.mark.parametrize(
    "isbn",
    ["123", "abcdefghij", "12345678901", None],
)
def test_validar_isbn10_rejeita_invalidos(isbn):
    assert validar_isbn10(isbn) is False


def test_normalizar_titulo_rejeita_none():
    with pytest.raises(ValueError):
        normalizar_titulo(None)