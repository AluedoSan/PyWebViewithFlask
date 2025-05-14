import sqlite3
"""
%Quantidade de bancos(nome, total, descrição)
%Caixinhas(descrição, valor, data)
%Tags(nome, descrição)
%User(nome, senha, email, data_nascimento)
"""
conn = sqlite3.connect('tutorial.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS bancos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    total REAL,
    descricao TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS caixinhas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT,
    valor REAL,
    data TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    descricao TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    senha TEXT,
    email TEXT,
    data_nascimento TEXT
)
''')

conn.commit()
conn.close()
print("Banco criado com sucesso!")
