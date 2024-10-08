class Pedido:
    def __init__(self, nome_pessoa, item_necessario, num_filhos, deficiente, mae_solteira, endereco, telefone):
        self.nome_pessoa = nome_pessoa
        self.item_necessario = item_necessario
        self.num_filhos = num_filhos
        self.deficiente = deficiente
        self.mae_solteira = mae_solteira
        self.endereco = endereco
        self.telefone = telefone
        self.prioridade = self.calcular_prioridade()

    def calcular_prioridade(self):
        # Exemplo simples de cálculo de prioridade
        prioridade = 0
        if self.deficiente:
            prioridade += 5
        if self.mae_solteira:
            prioridade += 2
        prioridade += self.num_filhos
        return prioridade

    def __str__(self):
        return f'{self.nome_pessoa} precisa de {self.item_necessario}.'
