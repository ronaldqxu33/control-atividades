
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from tarefa import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    excluir_tarefa,
    editar_tarefa
)


def adicionar():
    titulo = campo_tarefa.get().strip()
    nivel_prioridade = prioridade.get()

    if titulo == "":
        messagebox.showwarning("Atenção", "Digite uma tarefa.")
        return

    adicionar_tarefa(titulo, "", nivel_prioridade)

    campo_tarefa.delete(0, tk.END)
    prioridade.set("Média")
    atualizar_lista()


def atualizar_lista():
    lista_tarefas.delete(0, tk.END)

    tarefas = listar_tarefas()

    for tarefa in tarefas:
        if tarefa[4] == 1:
            status = "✓ Concluída"
        else:
            status = "○ Pendente"

        lista_tarefas.insert(
            tk.END,
            f"{tarefa[0]} - {tarefa[1]} | Prioridade: {tarefa[3]} | {status}"
        )


def concluir_selecionada():
    selecao = lista_tarefas.curselection()

    if not selecao:
        messagebox.showwarning("Atenção", "Selecione uma tarefa.")
        return

    tarefas = listar_tarefas()
    id_tarefa = tarefas[selecao[0]][0]

    concluir_tarefa(id_tarefa)
    atualizar_lista()


def excluir_selecionada():
    selecao = lista_tarefas.curselection()

    if not selecao:
        messagebox.showwarning("Atenção", "Selecione uma tarefa.")
        return

    confirmar = messagebox.askyesno(
        "Confirmar exclusão",
        "Tem certeza que deseja excluir esta tarefa?"
    )

    if not confirmar:
        return

    tarefas = listar_tarefas()
    id_tarefa = tarefas[selecao[0]][0]

    excluir_tarefa(id_tarefa)
    atualizar_lista()


def editar_selecionada():
    selecao = lista_tarefas.curselection()

    if not selecao:
        messagebox.showwarning(
            "Atenção",
            "Selecione uma tarefa para editar."
        )
        return

    novo_titulo = campo_tarefa.get().strip()

    if novo_titulo == "":
        messagebox.showwarning(
            "Atenção",
            "Digite o novo título da tarefa."
        )
        return

    tarefas = listar_tarefas()
    id_tarefa = tarefas[selecao[0]][0]

    editar_tarefa(id_tarefa, novo_titulo)

    campo_tarefa.delete(0, tk.END)
    atualizar_lista()

    messagebox.showinfo(
        "Sucesso",
        "Tarefa editada com sucesso!"
    )


def selecionar_tarefa(event):
    selecao = lista_tarefas.curselection()

    if not selecao:
        return

    tarefas = listar_tarefas()
    tarefa = tarefas[selecao[0]]

    campo_tarefa.delete(0, tk.END)
    campo_tarefa.insert(0, tarefa[1])


# Janela principal
janela = tk.Tk()
janela.title("Task Manager")
janela.geometry("800x650")
janela.resizable(False, False)
janela.configure(bg="#1e1e2e")


# Título
titulo = tk.Label(
    janela,
    text="atividaes RONALD",
    font=("segoe UI", 28, "bold"),
    bg="#1e1e2e",
    fg="white"
)
titulo.pack(pady=(30, 10))


# Subtítulo
subtitulo = tk.Label(
    janela,
    text="Organize suas tarefas e simplifique sua rotina",
    font=("Arial", 11),
    bg="#1e1e2e",
    fg="#b4b4c5"
)
subtitulo.pack()


campo_tarefa = tk.Entry(
    janela,
    font=("Segoe UI", 13),
    width=45,
    bg="#45475a",
    fg="white",
    insertbackground="white",
    relief="flat"
)
campo_tarefa.pack(pady=20)


# Prioridade
prioridade = ttk.Combobox(
    janela,
    values=["Alta", "Média", "Baixa"],
    state="readonly",
    font=("sagoe UI", 11),
    width=20
)

prioridade.set("Média")
prioridade.pack(pady=5)


# Botões
frame_botoes = tk.Frame(
    janela,
    bg="#1e1e2e"
)
frame_botoes.pack(pady=20)


botao_adicionar = tk.Button(
    frame_botoes,
    text="Adicionar tarefa",
    font=("sagoe UI", 10, "bold"),
    bg="#7c3aed",
    fg="white",
    padx=10,
    pady=8,
    command=adicionar
)
botao_adicionar.pack(side="left", padx=5)


botao_concluir = tk.Button(
    frame_botoes,
    text="Concluir tarefa",
    font=("sagoe UI", 10, "bold"),
    bg="#16a34a",
    fg="white",
    padx=10,
    pady=8,
    command=concluir_selecionada
)
botao_concluir.pack(side="left", padx=5)


botao_excluir = tk.Button(
    frame_botoes,
    text="Excluir tarefa",
    font=("sagoe UI", 10, "bold"),
    bg="#dc2626",
    fg="white",
    padx=10,
    pady=8,
    command=excluir_selecionada
)
botao_excluir.pack(side="left", padx=5)


botao_editar = tk.Button(
    frame_botoes,
    text="Editar tarefa",
    font=("sagoe UI", 10, "bold"),
    bg="#2563eb",
    fg="white",
    padx=10,
    pady=8,
    command=editar_selecionada
)
botao_editar.pack(side="left", padx=5)


# Lista visual de tarefas
lista_tarefas = tk.Listbox(
    janela,
    width=85,
    height=15,
    font=("Segoe UI", 11),
    bg="#313244",
    fg="#cdd6f4",
    selectbackground="#7c3aed",
    selectforeground="white",
    borderwidth=0,
    highlightthickness=0
)
lista_tarefas.pack(pady=20)

lista_tarefas.bind(
    "<<ListboxSelect>>",
    selecionar_tarefa
)


# Atualizar lista ao abrir
atualizar_lista()

# Manter janela aberta
janela.mainloop()
