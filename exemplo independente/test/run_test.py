from run import add2, divisao, informacoes


def test_add2():

    val = 5

    response = add2(val)

    assert response == 7


def test_divisao():
    val = 8
    resp = divisao(val)

    assert resp == 4
    assert isinstance(resp, float)


def test_informacoes():
    resp = informacoes()
    assert isinstance(resp, dict)
    assert "name" in resp
    assert "height" not in resp
    assert "Rafa" in resp["name"]
    assert resp["is_ok"]