
import sqlite3
from pathlib import Path

# Caminho do banco de dados
DB_DIR = Path(__file__).parent / "dados"
DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "tarefas.db"


# Conectar ao banco de dados
def conectar():
    return sqlite3.connect(DB_PATH)


# Criar tabela de tarefas
def criar_tabela():
    with conectar() as conexao:

        conexao.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                prioridade TEXT NOT NULL DEFAULT 'Média',
                concluida INTEGER NOT NULL DEFAULT 0,
                data_criacao TEXT
            )
        """)

        # Verificar se a coluna já existe
        colunas = conexao.execute(
            "PRAGMA table_info(tarefas)"
        ).fetchall()

        nomes_colunas = [coluna[1] for coluna in colunas]

        # Adicionar coluna caso não exista
        if "data_criacao" not in nomes_colunas:
            conexao.execute("""
                ALTER TABLE tarefas
                ADD COLUMN data_criacao TEXT
            """)

        # Preencher datas das tarefas antigas
        conexao.execute("""
            UPDATE tarefas
            SET data_criacao = CURRENT_TIMESTAMP
            WHERE data_criacao IS NULL
        """)


if __name__ == "__main__":
    criar_tabela()
    print("Banco de dados criado com sucesso!")

