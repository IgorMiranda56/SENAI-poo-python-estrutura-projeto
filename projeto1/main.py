import os
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa

os.system("cls || clear")

#Instanciando classe
pessoa1 = Pessoa(321, "Marta", "11/05/1995", "71 99999-9999", "mrt@gmail.com", 29, Sexo.FEMININO, Endereco("Rua A", 202, "Ap 101", "789", "Salvador", UnidadeFederativa.BAHIA))  
print(pessoa1)