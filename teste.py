import tkinter as tk
import sqlite3

# Função para salvar os valores no banco de dados
def salvar_valores():
    nome_pessoa = nome.get()
    valores = []
    
    camiseta_valor = f"Camiseta: {camiseta_quantidade.get()}"
    calca_valor = f"Calça: {calca_quantidade.get()}"
    casaco_valor = f"Casaco: {casaco_quantidade.get()}"
    
    valores.extend([camiseta_valor, calca_valor, casaco_valor])
    
    # Salva a lista no SQLite
    valores_str = ','.join(valores)
    cursor.execute('INSERT INTO Tabela2 (nome, valores) VALUES (?, ?)', (nome_pessoa, valores_str))
    conn.commit()
    print("Valores salvos no banco de dados.")

# Cria a janela
janela = tk.Tk()
janela.title("Entrada de Valores")

# Cria entrada para o nome da pessoa
nome_label = tk.Label(janela, text="Nome da Pessoa:")
nome_label.pack()
nome = tk.Entry(janela)
nome.pack()

# Cria as entradas
camiseta_label = tk.Label(janela, text="Camiseta:")
camiseta_label.pack()
camiseta_quantidade = tk.Entry(janela)
camiseta_quantidade.pack()

calca_label = tk.Label(janela, text="Calça:")
calca_label.pack()
calca_quantidade = tk.Entry(janela)
calca_quantidade.pack()

casaco_label = tk.Label(janela, text="Casaco:")
casaco_label.pack()
casaco_quantidade = tk.Entry(janela)
casaco_quantidade.pack()

# Botão para salvar os valores no banco de dados
botao = tk.Button(janela, text="Salvar Valores", command=salvar_valores)
botao.pack()

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('seu_banco_de_dados.db')
cursor = conn.cursor()

# Cria uma tabela para armazenar os valores
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tabela2 (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        valores TEXT
    )
''')

janela.mainloop()
