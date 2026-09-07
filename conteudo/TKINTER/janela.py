import tkinter as tk

def submit():
    #recupera os dados dos campos de entrada
    nome = nome_Entry.get()
    email = email_entry.get()

    #imprime os dados no console
    print(f"Nome: {nome}")
    print(f"Email: {email}")

#CRIA A JANELA PRINCIPAL
root = tk.Tk()
root.title("Formulário de aplicação")

#CRIA UM FRAME PARA OS WIDGETS
frame = tk.Frame(root)
frame.pack(padx= 10, pady=10)

#campo de entrada para NOME
nome_Entry = tk.Entry(frame)
nome_Entry.grid(row=0, column=1 )

#campo de entrada para EMAIL
email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)

#botao para SUBMISSAO
submit_button = tk.Button(frame, text='SUBMETER', command=submit)
submit_button.grid(row=2, columnspan=2, pady=10)

#Inicializa o loop da GUI
root.mainloop()