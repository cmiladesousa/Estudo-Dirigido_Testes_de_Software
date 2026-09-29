import unittest
from app_biblioteca.validators import (
    normalizar_titulo,
    validar_isbn10,
)


class TestValidators(unittest.TestCase):
    def test_validar_isbn10_aceita_10_digitos(self):
        self.assertTrue(validar_isbn10("1234567890"))

    def test_normalizar_titulo_remove_espacos(self):
        self.assertEqual(
            normalizar_titulo("  Teste   de   Software  "),
            "Teste de Software",
        )

    def test_normalizar_titulo_rejeita_none(self):
        with self.assertRaises(ValueError):
            normalizar_titulo(None)


if __name__ == "__main__":
    unittest.main()