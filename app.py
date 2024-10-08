import tkinter as tk
from tkinter import messagebox
from pedido import Pedido
from doacao import Doacao
from doador import Doador
from sistema_suporte import SistemaSuporteAlimentar


class SistemaApp:
    def __init__(self, master):
        self.master = master
        self.sistema = SistemaSuporteAlimentar()

        master.title("Sistema de Suporte Alimentar")
        master.state('zoomed')  # Maximizar a janela

        # Frames
        self.frame_pedido = tk.Frame(master)
        self.frame_doacao = tk.Frame(master)
        self.frame_verificar = tk.Frame(master)

        # Botões na parte superior
        self.botoes_frame = tk.Frame(master)
        self.botoes_frame.pack(side="top", fill="x")

        self.btn_fazer_pedido = tk.Button(self.botoes_frame, text="Fazer Pedido", command=self.show_frame_pedido,
                                          font=("Arial", 16))
        self.btn_fazer_pedido.pack(side="left", padx=20)

        self.btn_fazer_doacao = tk.Button(self.botoes_frame, text="Fazer Doação", command=self.show_frame_doacao,
                                          font=("Arial", 16))
        self.btn_fazer_doacao.pack(side="left", padx=20)

        self.btn_verificar_itens = tk.Button(self.botoes_frame, text="Verificar Itens Disponíveis",
                                             command=self.verificar_itens, font=("Arial", 16))
        self.btn_verificar_itens.pack(side="left", padx=20)

        # Iniciar com o frame de pedidos
        self.show_frame(self.frame_pedido)

        # Pedido Frame
        tk.Label(self.frame_pedido, text="Fazer um Pedido", font=("Arial", 24)).pack(pady=10)
        tk.Label(self.frame_pedido, text="Nome da pessoa que está pedindo", font=("Arial", 16)).pack()
        self.nome_pessoa_entry = tk.Entry(self.frame_pedido, font=("Arial", 16))
        self.nome_pessoa_entry.pack(pady=10)
        tk.Label(self.frame_pedido, text="O que está precisando?", font=("Arial", 16)).pack()
        self.item_necessario_entry = tk.Entry(self.frame_pedido, font=("Arial", 16))
        self.item_necessario_entry.pack(pady=10)
        tk.Label(self.frame_pedido, text="Quantos filhos tem?", font=("Arial", 16)).pack()
        self.num_filhos_entry = tk.Entry(self.frame_pedido, font=("Arial", 16))
        self.num_filhos_entry.pack(pady=10)
        self.deficiente_var = tk.BooleanVar()
        tk.Checkbutton(self.frame_pedido, text="Tem filhos com deficiência?", variable=self.deficiente_var,
                       font=("Arial", 16)).pack()
        self.mae_solteira_var = tk.BooleanVar()
        tk.Checkbutton(self.frame_pedido, text="É mãe solteira?", variable=self.mae_solteira_var,
                       font=("Arial", 16)).pack()
        tk.Label(self.frame_pedido, text="Endereço:", font=("Arial", 16)).pack()
        self.endereco_entry = tk.Entry(self.frame_pedido, font=("Arial", 16))
        self.endereco_entry.pack(pady=10)
        tk.Label(self.frame_pedido, text="Telefone:", font=("Arial", 16)).pack()
        self.telefone_entry = tk.Entry(self.frame_pedido, font=("Arial", 16))
        self.telefone_entry.pack(pady=10)
        tk.Button(self.frame_pedido, text="Enviar Pedido", command=self.enviar_pedido, font=("Arial", 16)).pack(pady=20)

        # Doação Frame
        tk.Label(self.frame_doacao, text="Fazer uma Doação", font=("Arial", 24)).pack(pady=10)
        tk.Label(self.frame_doacao, text="Nome do doador:", font=("Arial", 16)).pack()
        self.nome_doador_entry = tk.Entry(self.frame_doacao, font=("Arial", 16))
        self.nome_doador_entry.pack(pady=10)
        tk.Label(self.frame_doacao, text="Idade do doador:", font=("Arial", 16)).pack()
        self.idade_doador_entry = tk.Entry(self.frame_doacao, font=("Arial", 16))
        self.idade_doador_entry.pack(pady=10)
        tk.Label(self.frame_doacao, text="O que está doando?", font=("Arial", 16)).pack()
        self.item_doado_entry = tk.Entry(self.frame_doacao, font=("Arial", 16))
        self.item_doado_entry.pack(pady=10)
        tk.Button(self.frame_doacao, text="Enviar Doação", command=self.enviar_doacao, font=("Arial", 16)).pack(pady=20)

        # Verificar Frame
        tk.Label(self.frame_verificar, text="Itens Disponíveis", font=("Arial", 24)).pack(pady=10)
        self.resultado_label = tk.Label(self.frame_verificar, text="", font=("Arial", 16))
        self.resultado_label.pack(pady=10)
        tk.Button(self.frame_verificar, text="Voltar", command=self.show_frame_pedido, font=("Arial", 16)).pack(pady=20)

    def show_frame(self, frame):
        frame.pack(fill="both", expand=True)
        for f in (self.frame_pedido, self.frame_doacao, self.frame_verificar):
            if f != frame:
                f.pack_forget()

    def show_frame_pedido(self):
        self.show_frame(self.frame_pedido)

    def show_frame_doacao(self):
        self.show_frame(self.frame_doacao)

    def enviar_pedido(self):
        try:
            nome_pessoa = self.nome_pessoa_entry.get()
            item_necessario = self.item_necessario_entry.get()
            num_filhos = int(self.num_filhos_entry.get())
            deficiente = self.deficiente_var.get()
            mae_solteira = self.mae_solteira_var.get()
            endereco = self.endereco_entry.get()
            telefone = self.telefone_entry.get()

            pedido = Pedido(nome_pessoa, item_necessario, num_filhos, deficiente, mae_solteira, endereco, telefone)
            self.sistema.cadastrar_pedido(pedido)
            messagebox.showinfo("Sucesso", "Pedido enviado com sucesso!")
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def enviar_doacao(self):
        try:
            nome_doador = self.nome_doador_entry.get()
            idade = int(self.idade_doador_entry.get())
            item_doado = self.item_doado_entry.get()

            doador = Doador(nome_doador, idade)
            doacao = Doacao(item_doado, doador)
            self.sistema.receber_doacao(doacao)
            messagebox.showinfo("Sucesso", "Doação enviada com sucesso!")
            self.clear_entries_doador()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def verificar_itens(self):
        itens_disponiveis = self.sistema.distribuir_recursos()
        if not itens_disponiveis:
            self.resultado_label.config(text="Não há itens disponíveis.")
        else:
            resultados_texto = "Itens Disponíveis:\n\n"
            pedidos_atendidos = set()  # Para rastrear quais pedidos já foram atendidos
            doacoes_atendidas = set()  # Para rastrear quais doações já foram utilizadas

            for pedido_prioritario, doacao in itens_disponiveis:
                if pedido_prioritario in pedidos_atendidos or doacao in doacoes_atendidas:
                    continue  # Ignora se o pedido ou a doação já foram atendidos

                resultados_texto += (
                    f"Pedido: {pedido_prioritario.item_necessario}\n"
                    f"Nome da pessoa pedindo: {pedido_prioritario.nome_pessoa}\n"
                    f"Endereço: {pedido_prioritario.endereco}\n"
                    f"Telefone: {pedido_prioritario.telefone}\n"
                    f"Doação: {doacao.item}\n"
                    f"Nome do doador: {doacao.doador.nome}\n"
                )

                # Perguntar se a doação deve ser realizada
                fazer_doacao = messagebox.askyesno("Confirmação",
                                                   f"Realizar doação de {doacao.item} para {pedido_prioritario.nome_pessoa}?")
                if fazer_doacao:
                    pedidos_atendidos.add(pedido_prioritario)  # Marca o pedido como atendido
                    doacoes_atendidas.add(doacao)  # Marca a doação como utilizada
                    self.sistema.pedidos.remove(pedido_prioritario)
                    self.sistema.doacoes.remove(doacao)
                    messagebox.showinfo("Sucesso", "Doação realizada com sucesso!")

            self.resultado_label.config(text=resultados_texto)
        self.show_frame(self.frame_verificar)

    def clear_entries(self):
        self.nome_pessoa_entry.delete(0, tk.END)
        self.item_necessario_entry.delete(0, tk.END)
        self.num_filhos_entry.delete(0, tk.END)
        self.endereco_entry.delete(0, tk.END)
        self.telefone_entry.delete(0, tk.END)
        self.deficiente_var.set(False)
        self.mae_solteira_var.set(False)

    def clear_entries_doador(self):
        self.nome_doador_entry.delete(0, tk.END)
        self.idade_doador_entry.delete(0, tk.END)
        self.item_doado_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaApp(root)
    root.mainloop()
