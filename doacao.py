from doador import Doador

class Doacao:
    def __init__(self, item, doador):
        self.item = item
        self.doador = doador
    def __str__(self):
        return (f'Item: {self.item}, Doador: {self.doador.nome}')
