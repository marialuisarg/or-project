from tkinter import Tk, Label, Entry, Button, Frame

def add_row():
    # Cria um frame para armazenar as entradas de ponto de entrega e carga
    row_frame = Frame(data_frame)
    row_frame.pack(fill='x', pady=5)

    # Label para o ponto de entrega
    delivery_label = Label(row_frame, text="Ponto de Entrega:")
    delivery_label.pack(side='left', padx=5)

    # Campo para o ponto de entrega
    delivery_point = Entry(row_frame, width=20)
    delivery_point.pack(side='left', padx=5)

    # Label para a carga
    load_label = Label(row_frame, text="Carga:")
    load_label.pack(side='left', padx=5)

    # Campo para a carga
    load = Entry(row_frame, width=20)
    load.pack(side='left', padx=5)

    # Armazena a nova linha
    data_rows.append((delivery_point, load))

def gera_rotas():
    # Função que gera as rotas com base nas entradas
    for delivery_point, load in data_rows:
        ponto = delivery_point.get()
        carga = load.get()
        print(f"Ponto de entrega: {ponto}, Carga: {carga}")

if __name__ == '__main__':
    window = Tk()
    window.title("Gerador de Rotas de Entrega")
    window.config(padx=50, pady=50)

    # Frame para os dados, onde as linhas serão adicionadas
    data_frame = Frame(window)
    data_frame.pack(fill='both', expand=True)

    # Lista para armazenar as linhas de dados
    data_rows = []

    # Adiciona a primeira linha automaticamente ao iniciar
    add_row()

    # Frame inferior para os botões
    button_frame = Frame(window)
    button_frame.pack(side='bottom', fill='x', pady=10)

    # Botão para adicionar novas linhas de ponto de entrega e carga
    add_row_button = Button(button_frame, text="+", width=5, command=add_row)
    add_row_button.pack(side='left', padx=5)

    # Botão para gerar rotas
    add_button = Button(button_frame, text="Gerar rotas", width=36, command=gera_rotas)
    add_button.pack(side='right', padx=5)

    window.mainloop()
