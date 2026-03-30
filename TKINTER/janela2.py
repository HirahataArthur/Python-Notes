import tkinter as tk
from tkinter import messagebox

def submit():
    nome = nome_entry.get()
    email = email_entry.get()
    linguagem = linguagem_var.get()

    print(f"Nome: {nome}\nEmail: {email}\nLinguagem de preferência: {linguagem}")

root = tk.Tk()
root.title("--Formulario--")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

nome_Label = tk.Label(frame, text='Nome:') ##LABEL == LEGENDA
nome_Label.grid(row=0, column=0)


nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1)

email_label = tk.Label(frame, text="Email:")
email_label.grid(row=1, column=0)

email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)

## VAriavel para armazenar escolha da linguagem
linguagem_var = tk.StringVar(value="Python")

## RadioButton para Python
python_radio = tk.Radiobutton(frame, text="Python", variable=linguagem_var, value="Python")
python_radio.grid(row=2, column=0)

##Radiobutton para Java
java_radio = tk.Radiobutton(frame, text="Java", variable=linguagem_var, value="Java")
java_radio.grid(row=2, column=1)

##Botao de submissao 
submit_button = tk.Button(frame, text="Submeter", command=submit)
submit_button.grid(row=3, columnspan=2, pady=10)

root.mainloop()

