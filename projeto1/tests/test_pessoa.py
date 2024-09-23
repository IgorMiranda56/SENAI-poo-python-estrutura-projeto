import pytest
#from ..models.pessoa import Pessoa # Caminho relativo
#from projeto1.models.pessoa import Pessoa # Caminho relativo
from projeto1.models.pessoa import Pessoa 
from projeto1.models.endereco import Endereco 
from projeto1.models.enums.sexo import Sexo
from projeto1.models.enums.unidade_federativa import UnidadeFederativa

# Modelo.
@pytest.fixture
def criar_pessoa():
    pessoa1 = Pessoa(321, "Marta", "11/05/1995", "71 99999-9999", "mrt@gmail.com", 29, Sexo.FEMININO, 
                 Endereco("Rua A", 202, "Ap 101", "789", "Salvador", UnidadeFederativa.BAHIA))  
    return pessoa1

def test_pessoa_alterar_nome(criar_pessoa):
    #Alterando o nome da pessoa de 'Marta' para 'Vitoria'  
    criar_pessoa.nome = "Vitoria"
    assert criar_pessoa.nome == "Vitoria"

def test_pessoa_valido_nome(criar_pessoa):
    assert criar_pessoa.nome == "Marta"

def test_endereco_valido_logradouro_de_pessoa(criar_pessoa):
    assert criar_pessoa.endereco.logradouro == "Rua A"

def test_pessoa_idade_negativa(criar_pessoa):
    assert criar_pessoa.idade == 29

def test_pessoa_idade_negativa_retorna_mensagem_excecao(criar_pessoa):
    with pytest.raises(ValueError, match="Idade não pode ser negativa."): 
        Pessoa(321, "Marta", "11/05/1995", "71 99999-9999", "mrt@gmail.com", -29, Sexo.FEMININO, 
                 Endereco("Rua A", 202, "Ap 101", "789", "Salvador", UnidadeFederativa.BAHIA))  
    
