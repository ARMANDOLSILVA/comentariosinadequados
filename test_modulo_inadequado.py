import pytest
import inadequado 


def test_palavra_adequada():
    assert inadequado.palavraInadequada("dia") == False

def test_palavra_adequada_multiplo_case():
    assert inadequado.palavraInadequada("dIA") == False

def test_palavra_inadequada():
    assert inadequado.palavraInadequada("bosta") == True

def test_palavra_inadequada_multiplo_case():
    assert inadequado.palavraInadequada("bOstA") == True

def test_prepara_com_duas_palavras():
    prep = inadequado.preparaTexto("uM TextO")
    assert len(prep)==2 and ("um" in prep) and ("texto" in prep)

def test_prepara_texto_nulo():
    prep = inadequado.preparaTexto("")
    assert len(prep)==0 

def test_texto_inadequado():
    assert inadequado.textoInadequado("Um texto muito bosta") > 0.00

def test_texto_adequado():
    assert inadequado.textoInadequado("Um texto muito bom") == 0.00

def test_texto_inadequado_rapido():
    assert inadequado.textoInadequadoRapido("Um texto muito bosta") > 0.00

def test_texto_adequado_rapido():
    assert inadequado.textoInadequadoRapido("Um texto muito bom") == 0.00

def test_texto_inadequado_ou_adequado_com_texto_nulo():
    with pytest.raises(ZeroDivisionError):
        verifica = inadequado.textoInadequado("") 

def test_texto_inadequadorapido_ou_adequadorapido_com_texto_nulo():
    with pytest.raises(ZeroDivisionError):
        verifica = inadequado.textoInadequadoRapido("") 

def test_lista_palavras_inadequadas_ok():
    todalista = inadequado.listaPalavrasInadequadas
    totalmenteinadequado = " ".join(todalista)
    assert inadequado.textoInadequado(totalmenteinadequado) == 1.00

def test_lista_palavras_inadequadas_rapido_ok():
    todalista = inadequado.listaPalavrasInadequadas
    totalmenteinadequado = " ".join(todalista)
    assert inadequado.textoInadequadoRapido(totalmenteinadequado) > 0.00
