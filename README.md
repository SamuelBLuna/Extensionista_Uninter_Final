<<<<<<< HEAD
<h1 style="font-size: 50px;">Sistema de Suporte Alimentar</h1>

=======
   # SISTEMA DE SUPORTE ALIMENTAR
>>>>>>> 9268400493fb619b5eed3da74c6fe814a5d998fc
---

# Proposta do Projeto

Este projeto tem como objetivo criar um **Sistema de Suporte Alimentar** para ajudar famílias em situação de vulnerabilidade alimentar. O sistema foi desenvolvido para cadastrar pedidos de itens alimentares e receber doações, priorizando famílias conforme critérios estabelecidos para garantir que a ajuda chegue primeiro a quem mais necessita.

# Funcionalidades Principais

1. **Cadastro de Pedidos**: Pessoas podem registrar pedidos de itens alimentares, informando detalhes como o número de filhos, se há crianças com deficiência, se são mães solteiras, além de fornecer nome, endereço e telefone.
2. **Registro de Doações**: Doadores podem cadastrar suas doações, informando o nome, idade e o item que desejam doar.
3. **Verificação e Distribuição de Itens**: O sistema verifica se há doações disponíveis e faz o cruzamento com os pedidos cadastrados. A distribuição de recursos segue critérios de prioridade.

---

# Critérios de Prioridade para Doações

Quando uma doação é registrada, o sistema organiza os pedidos de acordo com os seguintes critérios, em ordem de prioridade:

1. **Filhos com deficiência**: Famílias com filhos com deficiência têm prioridade máxima.
2. **Mães solteiras**: Se houver empate no critério anterior, mães solteiras terão preferência.
3. **Número de filhos**: Em caso de empate nos dois primeiros critérios, famílias com mais filhos serão priorizadas.

Após a verificação, o sistema exibe os itens disponíveis e permite ao usuário decidir se a doação será realizada naquele momento. O item doado é removido do sistema assim que a doação for confirmada.

---

# Como Clonar o Projeto

Para clonar e executar este projeto em sua máquina local, siga os passos abaixo:

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/SamuelBLuna/Extensionista_Uninter_Final.git
   cd Extensionista_Uninter_Final
2. **Instalar dependências:** O projeto utiliza a biblioteca Tkinter para a interface gráfica, que já vem instalada por padrão na maioria das distribuições do Python. No entanto, é recomendável instalar o ambiente virtual e ativá-lo para garantir que todas as dependências sejam instaladas corretamente.
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
3. **Executar o projeto:** Para iniciar o sistema, execute o arquivo principal `app.py`:
    ```bash
    python app.py

---

# Bibliotecas Utilizadas

O projeto utiliza as seguintes bibliotecas:
* Tkinter: Para a criação da interface gráfica. Tkinter é a biblioteca padrão para GUIs no Python, sendo fácil de usar e altamente eficiente para aplicativos desktop.
    ```python
    import tkinter as tk
    from tkinter import messagebox

---

# Exemplo de Funcionamento do Sistema
1. **Fazer um Pedido:**
    * Nome: Maria Antônia
    * Item Necessário: Cesta Basica
    * Número de filhos: 2
    * Tem filhos com deficiência: Sim
    * É mãe solteira: Não
    * Endereço: Rua São Paulo, 123
    * Telefone: (99) 99999-9999

---

2. **Fazer uma Doação:**
    * Nome do Doador: Maria
    * Idade: 40 anos
    * Item: Cesta Basica

---

3. **Verificar Itens Disponíveis:**
Ao verificar os itens disponíveis, o sistema exibirá os detalhes do pedido e do doador. Após isso, será perguntado ao usuário se deseja realizar a doação naquele momento. Se confirmada, o pedido e a doação são removidos do sistema.

---

# Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

# Licença

[![Licença MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Este projeto está sob a licença MIT. Para mais informações, veja o arquivo <a src="https://pt.wikipedia.org/wiki/Licen%C3%A7a_MIT">LICENSE.</a>

---

# Itens a Serem Melhorados na Próxima Versão
Na próxima versão do sistema, será dada especial atenção às seguintes melhorias:

1. **Aprimoramento da Tela de Verificação de Itens Disponíveis:**
    * A tela de verificação de itens será aprimorada para exibir todos os itens disponíveis de maneira mais intuitiva, listando cada item em uma linha, com os detalhes do doador e da pessoa que solicitou o item. Cada item terá dois botões: Doar Agora e Aguardar, permitindo ao usuário uma escolha mais clara e organizada sobre as doações.

2. **Design e Layout da Interface (Payate do Programa):**
    * Será implementado um design mais elegante e funcional, com melhor distribuição de componentes na interface gráfica. O layout será otimizado para melhorar a experiência do usuário, facilitando o uso do sistema tanto para os que desejam pedir ajuda quanto para os doadores.
