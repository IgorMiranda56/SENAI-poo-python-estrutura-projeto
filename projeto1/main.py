import os
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidadeFederativa import UnidadeFederativa

os.system("cls || clear")

#Instanciando classe
pessoa1 = Pessoa("Marta", 22, Sexo.FEMININO, Endereco("Rua A", 35, UnidadeFederativa.BAHIA))

print(pessoa1)