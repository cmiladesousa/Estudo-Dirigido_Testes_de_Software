import pytest
from run import func_de_erro


def test_error():
    try:
        func_de_erro()
    except Exception as exception:
        assert str(exception) == "Meu Erro esta aqui"


def test_error_with_pytest():
    with pytest.raises(Exception) as error_info:
        func_de_erro()
    assert str(error_info.value) == "Meu Erro esta aqui"