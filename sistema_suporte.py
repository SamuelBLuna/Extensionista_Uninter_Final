from pedido import Pedido
from doacao import Doacao

class SistemaSuporteAlimentar:
    def __init__(self):
        self.pedidos = []  # Lista de pedidos
        self.doacoes = []  # Lista de doações

    def cadastrar_pedido(self, pedido):
        self.pedidos.append(pedido)
        print(f'Pedido registrado: {pedido.nome_pessoa} está esperando por {pedido.item_necessario}.')

    def receber_doacao(self, doacao):
        self.doacoes.append(doacao)
        print(f'Doação de {doacao.item} recebida de {doacao.doador.nome}.')

    def distribuir_recursos(self):
        if not self.doacoes:
            print("Nenhuma doação disponível no momento.")
            return []

        distribuicoes = []  # Lista para armazenar as distribuições realizadas

        for doacao in self.doacoes:
            # Filtra pedidos correspondentes ao item doado
            pedidos_correspondentes = [pedido for pedido in self.pedidos if pedido.item_necessario == doacao.item]

            if not pedidos_correspondentes:
                continue  # Se não houver pedidos correspondentes, continua para a próxima doação

            # Ordenar pedidos por prioridade
            pedidos_ordenados = sorted(pedidos_correspondentes, key=lambda p: (-p.prioridade, p.num_filhos))

            # Mostra o pedido com maior prioridade
            pedido_prioritario = pedidos_ordenados[0]
            distribuicoes.append((pedido_prioritario, doacao))  # Adiciona à lista de distribuições

        return distribuicoes  # Retorna as distribuições realizadas
