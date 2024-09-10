from models.enums.unidadeFederativa import UnidadeFederativa


class Endereco:
    def __init__(self, logradouro: str, numero: int, uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.uf = uf
    
    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nUnidade Federativa: {self.uf.value}")