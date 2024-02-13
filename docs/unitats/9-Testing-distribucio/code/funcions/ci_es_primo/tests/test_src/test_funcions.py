from src.funcions import es_primo


def test_primo_1():
    assert es_primo(1) == False
    
def test_primo_2():
    assert es_primo(2) == True

def test_es_primo_negativo():
    assert es_primo(-10) == False
    assert es_primo(0) == False

def test_es_primo_numero_no_primo_mayor_2():
   assert es_primo(4) == False

def test_es_primo_numero_primo_mayor_2():
   assert es_primo(27) == False