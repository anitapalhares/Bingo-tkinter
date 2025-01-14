import random
import tkinter as tk

root = tk.Tk() 
root.title("My Bingo Program")
root.geometry("800x800")
    
root.configure(bg='#267326')  # Cor de fundo da janela principal
label = tk.Label(root, text="Bem-vindo ao Bingo!", bg='white', font=("Arial", 16))
label.grid(row=0, column=0, columnspan=5, rowspan=1, sticky="nsew")


# Criar a grade de 5x5
for row in range(5):
    for col in range(5):
        # Criar botões para cada célula
        btn = tk.Button(root, text="", width=8, height=3, bg="lightgray")
        btn.grid(row=row+1, column=col, padx=5, pady=5)  # Adicionar o botão ao grid


root.mainloop()

for row in range(5):
    for col in range(5):
        if row == 2 and col == 2:  # Célula central (linha 3, coluna 3)
            btn = tk.Button(root, text="BINGO", width=8, height=3, bg="yellow", state="disabled", font=("Arial", 10, "bold"))
        else:
            btn = tk.Button(root, text="", width=8, height=3, bg="lightgray")
        btn.grid(row=row+1, column=col, padx=5, pady=5)  # Desloca a grade para baixo

# Configurar a expansão das células da grade
for row in range(6):  # Incluímos a linha do Label
    root.grid_rowconfigure(row, weight=1)
for col in range(5):
    root.grid_columnconfigure(col, weight=1)




