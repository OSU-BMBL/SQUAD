
from squad_py.example import test

def test_smoke():
    res = test()
    assert res == "Hello World!"
