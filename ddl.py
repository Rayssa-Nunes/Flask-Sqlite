import sqlite3
from flask import g
from Globals import DATABASE_NAME

# Função para conexão com o banco de dados
def get_db(): 
    db = getattr(g, '_database', None)  # O objeto g é usado para armazenar dados que podem ser
                                        # usados sempre que forem chamados no contexto do aplicativo
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_NAME)
        db.row_factory = sqlite3.Row
    return db

# Função para fechar conexão com o banco de dados quando o contexto termina
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Função para inicializar o banco de dados baseado no esquema definido
def init_db():
    db = get_db()
    with open('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()