from models.enums.sexo import Sexo
from models.endereco import Endereco

class Pessoa:
    def __init__(self, id:int, nome: str, dataNascimento: str, telefone: str, email: str, idade: int, sexo: Sexo, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.email = email
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"\nId: {self.id} \nNome: {self.nome} \nData de Nascimento: {self.dataNascimento} \nTelefone: {self.telefone} \nEmail: {self.email} \nIdade: {self.idade} \nSexo: {self.sexo.texto} {self.sexo.caracter}  \nEndereço: {self.endereco}")