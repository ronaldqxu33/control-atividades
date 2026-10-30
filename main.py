
from tarefa import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    excluir_tarefa
)

from database import criar_tabela


def exibir_menu():

    print("\n===== TASK MANAGER =====")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - data de criaçao")
    print("0 - Sair")


def main():
    criar_tabela()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição: ")

            print("Prioridades: Baixa, Média ou Alta")
            prioridade = input("Escolha a prioridade: ").capitalize()

            if prioridade not in ["Baixa", "Média", "Alta"]:
                print("Prioridade inválida!")
                continue

            if not titulo.strip():
                print("O título não pode ficar vazio!")
                continue

            adicionar_tarefa(titulo, descricao, prioridade)

        elif opcao == "2":
            tarefas = listar_tarefas()

            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for tarefa in tarefas:
                    status = "Concluída" if tarefa[4] else "Pendente"

                    print(f"\nID: {tarefa[0]}")
                    print(f"Título: {tarefa[1]}")
                    print(f"Descrição: {tarefa[2]}")
                    print(f"Prioridade: {tarefa[3]}")
                    print(f"Data de criacao: {tarefa[5]}")
                    print(f"Status: {status}")

        elif opcao == "3":
            id_tarefa = input("Digite o ID da tarefa: ")

            if id_tarefa.isdigit():
                concluir_tarefa(int(id_tarefa))
            else:
                print("Digite um ID válido!")

        elif opcao == "4":
            id_tarefa = input("Digite o ID da tarefa: ")

            if id_tarefa.isdigit():
                excluir_tarefa(int(id_tarefa))
            else:
                print("Digite um ID válido!")

        elif opcao == "0":
            print("Encerrando o Task Manager...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
