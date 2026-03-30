import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Configuração da janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro de Alunos")
janela.geometry("820x600")

# Definição das colunas da tabela
COLUNAS = ("Aluno", "Nota1", "Nota2", "Média", "Situação")

# Widgets de entrada
lblNome = tk.Label(janela, text="Nome do Aluno:")
txtNome = tk.Entry(janela, bd=3)

lblNota1 = tk.Label(janela, text="Nota 1:")
txtNota1 = tk.Entry(janela)

lblNota2 = tk.Label(janela, text="Nota 2:")
txtNota2 = tk.Entry(janela)

# Posicionamento com grid
lblNome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
txtNome.grid(row=0, column=1, padx=5, pady=5)

lblNota1.grid(row=1, column=0, padx=5, pady=5, sticky="w")
txtNota1.grid(row=1, column=1, padx=5, pady=5)

lblNota2.grid(row=2, column=0, padx=5, pady=5, sticky="w")
txtNota2.grid(row=2, column=1, padx=5, pady=5)

# Botão de cadastro
btnCadastrar = tk.Button(janela, text="Cadastrar", command=lambda: cadastrar_aluno())
btnCadastrar.grid(row=3, column=0, columnspan=2, pady=10)

# Tabela Treeview
treeMedias = ttk.Treeview(janela, columns=COLUNAS, show="headings")
for coluna in COLUNAS:
    treeMedias.heading(coluna, text=coluna)
    treeMedias.column(coluna, width=120)

treeMedias.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Scrollbar
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=treeMedias.yview)
treeMedias.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=4, column=2, sticky="ns")

# Funções
def verificar_situacao(n1, n2):
    media = (n1 + n2) / 2
    if media >= 7.0:
        return media, "Aprovado"
    elif media >= 5.0:
        return media, "Em Recuperação"
    return media, "Reprovado"

def cadastrar_aluno():
    try:
        nome = txtNome.get().strip()
        nota1 = float(txtNota1.get())
        nota2 = float(txtNota2.get())

        if not nome:
            messagebox.showwarning("Aviso", "Digite o nome do aluno.")
            return

        media, situacao = verificar_situacao(nota1, nota2)
        treeMedias.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao))
        salvar_dados()

    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos para as notas.")
    finally:
        txtNome.delete(0, "end")
        txtNota1.delete(0, "end")
        txtNota2.delete(0, "end")

def salvar_dados():
    dados = [treeMedias.item(line)["values"] for line in treeMedias.get_children()]
    df = pd.DataFrame(data=dados, columns=COLUNAS)
    try:
        df.to_excel("planilhaAlunos.xlsx", index=False)
        print("Dados salvos com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro ao salvar", str(e))

def carregar_dados_iniciais():
    try:
        df = pd.read_excel("planilhaAlunos.xlsx")
        for _, row in df.iterrows():
            treeMedias.insert("", "end", values=(row["Aluno"], row["Nota1"], row["Nota2"], row["Média"], row["Situação"]))
    except FileNotFoundError:
        print("Nenhum dado encontrado.")
    except Exception as e:
        messagebox.showerror("Erro ao carregar dados", str(e))

# Carregar dados ao iniciar
carregar_dados_iniciais()

# Loop principal
janela.mainloop()