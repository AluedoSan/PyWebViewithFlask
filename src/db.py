import sqlite3
from flask import g
from main import server

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(server.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

def criar_usuario(email, senha):
    db = get_db()
    db.execute("INSERT INTO user (email, senha) VALUES (?, ?)", (email, senha))
    db.commit()
    
def get_user_by_email(email):
    db = get_db()
    return db.execute('SELECT * FROM user WHERE email = ?', (email,)).fetchone()
    
@server.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()