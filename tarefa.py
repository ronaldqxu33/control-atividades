
from database import conectar


# Cadastrar uma nova tarefa
def adicionar_tarefa(titulo, descricao, prioridade):
    with conectar() as conexao:
        conexao.execute("""
            INSERT INTO tarefas (titulo, descricao, prioridade, data_criacao)
            VALUES (?, ?, ?, datetime('now', 'localtime'))
        """, (titulo, descricao, prioridade))

    print("Tarefa cadastrada com sucesso!")


# Listar todas as tarefas
def listar_tarefas():
    with conectar() as conexao:
        tarefas = conexao.execute("""
            SELECT * FROM tarefas
        """).fetchall()

    return tarefas


# Concluir uma tarefa
def concluir_tarefa(id_tarefa):
    with conectar() as conexao:
        cursor = conexao.execute("""
            UPDATE tarefas
            SET concluida = 1
            WHERE id = ?
        """, (id_tarefa,))

    if cursor.rowcount > 0:
        print("Tarefa concluída com sucesso!")
    else:
        print("Tarefa não encontrada!")


# Excluir uma tarefa
def excluir_tarefa(id_tarefa):
    with conectar() as conexao:
        cursor = conexao.execute("""
            DELETE FROM tarefas
            WHERE id = ?
        """, (id_tarefa,))

    if cursor.rowcount > 0:
        print("Tarefa excluída com sucesso!")
    else:
        print("Tarefa não encontrada!")
def editar_tarefa(id_tarefa, novo_titulo):
    with conectar() as conexao:
        conexao.execute("""
            UPDATE tarefas
            SET titulo = ?
            WHERE id = ?
        """, (novo_titulo, id_tarefa))

    print("Tarefa atualizada com sucesso!")

