from tkinter import Tk, Label, Entry, Button, Frame, StringVar, Listbox, Scrollbar, messagebox
import maps_api_handler as mp
import solver as glpk

delivery_points_dict = {
    "Petrópolis":"ChIJX8jgemIAmQARqkMTFntxVf0",
    "Rio Pomba":"ChIJ3Swriwv4ogAR1LEPOKSjZ5o",
    "Ubá":"ChIJ0dkPI1oZowARMdqbTYsZmzE",
    "Visconde do Rio Branco":"ChIJ1zehpdk9owARVqGBQ-NzbpY",
    "Viçosa":"ChIJDyh5e5VnowARBtrMLiCtJU4",
    "Ponte Nova":"ChIJ-652eHaWpAARM0GeV0nRr74",
    "João Monlevade":"ChIJFVR2MkcHpQARmru5TDcVVuc",
    "Ipatinga":"ChIJ_5ooqef_rwAR9BHO0LyuBI8",
    "Coronel Fabriciano":"ChIJSYOTJClUpQARvHGo6NMc3Go",
    "Timóteo":"ChIJ6fC4_1tRpQARS0rcoxDI-XU",
    "Itabira":"ChIJS7521hOhpQAR14IVxfgdGwo",
    "Sabará":"ChIJ2zKlf-6CpgARhBqlFNbAZv4",
    "Santa Luzia":"ChIJ6_jwB7GGpgARU4LSfsUnRf8",
    "Vespasiano":"ChIJpdUMsC-GpgARI6lR8rxw-Tw",
    "Ribeirão das Neves":"ChIJu0dmzmWNpgARhXfApDB5tfY",
    "Belo Horizonte":"ChIJMyzPysqQpgARlznSOl55NVs",
    "Conselheiro Lafaiete":"ChIJZ8e3oujfowARSB1ergAuecY",
    "Barbacena":"ChIJxzZvpXX1oQAR4oSg6EuCKzU",
    "Santos Dumont":"ChIJ045wRA8SogARDMhhJworWD0",
    "Três Rios":"ChIJkzN9tpBemAARfRvLO8RAeso",
    "Paraíba do Sul":"ChIJszo-un_wmAAR4TqYcp2tI5g",
    "Vassouras":"ChIJhxFVCugwmQARvpiOzd5t6xs",
    "Barra do Piraí":"ChIJJSkTPwS1ngARn4D5_sxZqtU",
    "Volta Redonda":"ChIJHVxOS6yingARIq38VpO8ddQ",
    "Barra Mansa":"ChIJK6bP2fibngARI63HZEPD21Y",
    "Resende":"ChIJlfVB1Y13ngARgd8VmvS2Izg",
    "Cruzeiro":"ChIJx1My53_2nQARFxAbXnbB0Rc",
    "Lorena":"ChIJ34pGHSDJzJQRIsZGRUuczsk",
    "Guaratinguetá":"ChIJCSsYLz3EzJQRpylKXb1e-U8",
    "Taubaté":"ChIJOw2vGVr4zJQRH7Sy3bFCykk",
    "Aparecida do Norte":"ChIJHdHQfTzDzJQRxAiT_DNA1-k",
    "SÃO PAULO":"ChIJ0WGkg4FEzpQRrlsz_whLqZs",
    "Itajubá":"ChIJBZ3uQIJjy5QRnadsNDAmeJw",
    "Varginha":"ChIJPT3hD0ONypQR_ZwxXxQ0NeM",
    "Três Corações":"ChIJm4Vq--DcypQRpUavWMNPxkc",
    "São Lourenço":"ChIJuTbNZpFLy5QROXIpjLeEghU",
    "Caxambu":"ChIJC8wNnqUmngARMkMU7MEHDLI",
    "Baependi":"ChIJb588fQclngARFe0PuuB6gCE",
    "Argirita":"ChIJeXSVyta9ogARcCovV0mXhBY",
    "Leolpoldina":"ChIJ34wYc3HJogARE1_MnRGRiV4",
    "Muriaé":"ChIJF0ozUkHGvAARzFA381YWSFk",
    "Itaperuna":"ChIJLeXUIG9gvAARqmuPj875Njg",
    "Italva":"ChIJ2YKJz_FFvAAR7druop4TB_U",
    "Campos":"ChIJRbWBvtHVvQAR4Y4W5zaxl-4",
    "Macaé":"ChIJO0REeCYwlgARWd7QP-jRQJg",
    "Rio das Ostras":"ChIJh9TQq9m0lwARsrQhfwMk3xo",
    "São Pedro da Aldeia":"ChIJr32UWpQPlwARcSs3WMplQtU",
    "Araruama":"ChIJ-6YPcGBplwARPMyE_X9my94",
    "RJ - Madureira":"ChIJH8zPKChjmQARSA7rbY46qI4",
    "RJ - Taquara":"ChIJRx5f1N_YmwAR9z4Bicgmd_k",
    "RJ - Freguesia":"ChIJGUxD_DzYmwAR1a2TcSDlsrI",
    "RJ - Engenho da Rainha":"ChIJPe_UtI58mQARJbfU4q2_2yY",
    "RJ - Tijuca":"ChIJzdr7Sxt-mQARGBb529c4TUo",
    "RJ - Centro":"ChIJF3IcFV5_mQARfbkw_ML5_X8",
    "RJ - Copacabana":"ChIJU5wP0iPVmwARDWteYzJhPGk",
    "RJ - Ipanema":"ChIJkWFy_g_VmwARe6ZZnNoVArs",
    "RJ - Meier":"ChIJdQKoPaV9mQARW8BsrPR-ilA",
    "RJ - Engenho de Dentro":"ChIJLRaSlgx9mQARfLjMlrXsl-Y",
    "RJ - Recreio":"ChIJsVhyWKrCmwAROv2KZeNUQQk",
    "RJ - Vargem Grande":"ChIJ6QL9t3_dmwARUbXw8UhpII0",
    "RJ - Vargem Pequena":"ChIJDQXL4aDdmwARLDyc7aWEfC8",
    "RJ - Barra da Tijuca":"ChIJXf62J0ramwARTg-e2NH2w2M",
    "RJ - Bonsucesso":"ChIJVV3hfQF8mQARfyAUTn9KclA",
    "RJ - São João de Meriti":"ChIJe-aj_VRkmQARowMWVBdMP3o",
    "RJ - Nilópolis":"ChIJbbtGb1JhmQARoq2k96s9VtI",
    "RJ - Mesquita":"ChIJLXOC-dZgmQARkh8-kC1RJlE",
    "RJ - Belford Roxo":"ChIJaTNJK25vmQARcMLcTsC0f7s"
}

data_rows = []
selected_cities = []

def create_custom_dropdown(parent, variable, options):
    def toggle_menu():
        if listbox_frame.winfo_ismapped():
            listbox_frame.pack_forget()
        else:
            listbox_frame.pack(fill='x')

    button = Button(parent, textvariable=variable, command=toggle_menu, width=20, relief="raised")
    button.pack(side='left')

    listbox_frame = Frame(parent)

    scrollbar = Scrollbar(listbox_frame)
    scrollbar.pack(side='right', fill='y')

    listbox = Listbox(listbox_frame, yscrollcommand=scrollbar.set, height=5)
    
    filtered_options = [option for option in options if option not in selected_cities]
    for option in filtered_options:
        listbox.insert('end', option)
    listbox.pack(fill='both', expand=True)

    scrollbar.config(command=listbox.yview)

    def select_option(event):
        if listbox.curselection():
            selection = listbox.get(listbox.curselection())
            variable.set(selection)
            selected_cities.append(selection) 
            listbox_frame.pack_forget()

    listbox.bind("<<ListboxSelect>>", select_option)

    return button, listbox_frame

def add_row():
    row_frame = Frame(data_frame)
    row_frame.pack(fill='x', pady=5)

    delivery_label = Label(row_frame, text="Ponto de Entrega:")
    delivery_label.pack(side='left', padx=5)

    delivery_point_var = StringVar(row_frame)
    
    available_cities = ["Selecione uma cidade"]
    available_cities.append(city for city in delivery_points_dict.keys() if city not in selected_cities)
    if not available_cities:
        messagebox.showinfo("Info", "Não há mais pontos de entrega disponíveis.")
        return

    delivery_point_var.set(available_cities[0])

    delivery_point_menu, listbox_frame = create_custom_dropdown(row_frame, delivery_point_var, delivery_points_dict.keys())
    delivery_point_menu.pack(side='left', padx=5)

    load_label = Label(row_frame, text="Carga (P/M/G):")
    load_label.pack(side='left', padx=5)

    load_P = Entry(row_frame, width=5)
    load_P.pack(side='left', padx=5)

    load_M = Entry(row_frame, width=5)
    load_M.pack(side='left', padx=5)

    load_G = Entry(row_frame, width=5)
    load_G.pack(side='left', padx=5)

    data_rows.append((delivery_point_var, load_P, load_M, load_G))

def get_distance_matrix():
    ids_list = []
    volume_list = []
    total_volume = 0

    ids_list.append("place_id:ChIJoV344UOcmAARaKSgsyawNmI") 
    volume_list.append(0) 

    for row in data_rows:
        delivery_point_var, load_P, load_M, load_G = row
        delivery_point = delivery_point_var.get()

        try:
            p_volume = max(int(load_P.get()), 0) * 0.0025
            m_volume = max(int(load_M.get()), 0) * 0.01
            g_volume = max(int(load_G.get()), 0) * 0.054
        except ValueError:
            messagebox.showerror("Erro", "Quantidade de caixas inválida, deve ser um número.")
            return

        point_volume = p_volume + m_volume + g_volume
        total_volume += point_volume

        if delivery_point in delivery_points_dict:
            ids_list.append("place_id:" + delivery_points_dict[delivery_point])
        else:
            messagebox.showerror("Erro", f"Ponto de entrega '{delivery_point}' não encontrado no dicionário.")
            return

        volume_list.append(point_volume)

        if total_volume > 15:
            messagebox.showerror("Erro", f"O volume total ({total_volume:.2f} m³) excede o limite do veículo de 15 m³.")
            return

    dist_matrix, time_matrix = mp.build_url(ids_list)

    model = glpk.create_model(len(dist_matrix), dist_matrix, volume_list)
    
    mp.plot_result(ids_list, model)

if __name__ == '__main__':
    window = Tk()
    window.title("Gerador de Rotas de Entrega")
    window.config(padx=50, pady=50)

    data_frame = Frame(window)
    data_frame.pack(fill='both', expand=True)

    add_row_button = Button(window, text="Adicionar Ponto de Entrega", command=add_row)
    add_row_button.pack(pady=10)

    get_distance_button = Button(window, text="Gerar Rota", command=get_distance_matrix)
    get_distance_button.pack(pady=10)

    window.mainloop()