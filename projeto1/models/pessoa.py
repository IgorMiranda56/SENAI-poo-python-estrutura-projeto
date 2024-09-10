from models.enums.sexo import Sexo
from models.endereco import Endereco

class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"\nNome: {self.nome} \nIdade: {self.idade} \nSexo: {self.sexo.value} \nEndereço: {self.endereco}")