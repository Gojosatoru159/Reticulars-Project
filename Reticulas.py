import tkinter as tk
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def generate_relation():
    global relation_matrix
    relation_matrix = np.random.randint(2, size=(len(set_A), len(set_A))) # creo matriz
    #para que no se apunte asi mismo 
    for i in range(len(relation_matrix)):
        for j in range(len(relation_matrix[i])):
            if i == j:
                relation_matrix[i, j] = 0
    # relation_matrix = [
    #     [1, 0, 0, 1, 0, 0],
    #     [0, 1, 0, 1, 0, 0],
    #     [1, 0, 1, 1, 0, 0],
    #     [0, 0, 0, 1, 0, 0],
    #     [1, 1, 1, 1, 1, 1],
    #     [0, 1, 0, 1, 0, 1]
    # ]
    update_relation_display()
    generate_hasse_diagram()

def update_relation_display():
    relation_text.config(state=tk.NORMAL)
    relation_text.delete('1.0', tk.END)
    for i, row in enumerate(relation_matrix):
        for j, value in enumerate(row):
            if value == 1:
                relation_text.insert(tk.END, f'({set_A[i]}, {set_A[j]})\n')
    relation_text.config(state=tk.DISABLED)

    text = str(relation_matrix)
    text = text[1:-1]
    text = " " + text

    matrix_text.config(state=tk.NORMAL)
    matrix_text.delete('1.0', tk.END)
    matrix_text.insert(tk.END, text)
    matrix_text.config(state=tk.DISABLED)

def check_partial_order():
    is_partial_order = True
    
    for i in range(len(set_A)):
        for j in range(i + 1, len(set_A)):
            if relation_matrix[i][j] == 1 and relation_matrix[j][i] == 1:
                is_partial_order = False
                break
    
    partial_order_label.config(text=f"Es orden parcial: {is_partial_order}")

def check_lattice():
    is_lattice = True
    
    for i in range(len(set_A)):
        for j in range(len(set_A)):
            if relation_matrix[i][j] != relation_matrix[j][i]:
                is_lattice = False
                break
    
    lattice_label.config(text=f"Es retícula: {is_lattice}")

def generate_hasse_diagram():
    G = nx.DiGraph()
    #print(relation_matrix[1, 2])
    #print(relation_matrix)
    #print(G)
    for i, row in enumerate(relation_matrix):
        for j, value in enumerate(row):
            if value == 1:
                G.add_edge(set_A[i], set_A[j])
    
    pos = nx.shell_layout(G)  # Cambia el algoritmo de diseño si es necesario
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrows=False)
    plt.title("Diagrama de Hasse")
    plt.axis("off")
    plt.show()

def submit_elements():
    global set_A
    set_A = elements_entry.get().split()
    relation_text.config(state=tk.NORMAL)
    relation_text.delete('1.0', tk.END)
    relation_text.config(state=tk.DISABLED)
    matrix_text.config(state=tk.NORMAL)
    matrix_text.delete('1.0', tk.END)
    matrix_text.config(state=tk.DISABLED)
    partial_order_label.config(text="")
    lattice_label.config(text="")
    elements_label.config(text=f"Elementos del conjunto A: {set_A}")

# Inicialización de la interfaz gráfica
root = tk.Tk()
root.title("Relación, Retícula y Diagrama de Hasse")

set_A = []
relation_matrix = []

elements_label = tk.Label(root, text="Ingrese elementos del conjunto A:")
elements_label.pack()

elements_entry = tk.Entry(root)
elements_entry.pack()

submit_button = tk.Button(root, text="Enviar", command=submit_elements)
submit_button.pack()

generate_button = tk.Button(root, text="Generar Relación Aleatoria", command=generate_relation)
generate_button.pack()

relation_text = tk.Text(root, height=10, width=30, state=tk.DISABLED)
relation_text.pack()

matrix_text = tk.Text(root, height=10, width=30, state=tk.DISABLED)
matrix_text.pack()

partial_order_button = tk.Button(root, text="Verificar Orden Parcial", command=check_partial_order)
partial_order_button.pack()

partial_order_label = tk.Label(root, text="")
partial_order_label.pack()

lattice_button = tk.Button(root, text="Verificar Reticula", command=check_lattice)
lattice_button.pack()

lattice_label = tk.Label(root, text="")
lattice_label.pack()

root.mainloop()