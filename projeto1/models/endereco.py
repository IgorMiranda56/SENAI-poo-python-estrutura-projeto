from models.enums.unidade_federativa import UnidadeFederativa


class Endereco:
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
    
    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nComplento: {self.complemento} \nCEP: {self.cep} \nCidade: {self.cidade} \nUnidade Federativa: {self.uf.texto}")