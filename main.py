from tkinter import Tk, Label, Entry, Button, Frame, StringVar, OptionMenu
import maps_api_handler as mp

# Dicionário que associa nome do ponto de entrega a um id
delivery_points_dict = {
    "Petrópolis":"ChIJX8jgemIAmQARqkMTFntxVf0",
    "JUIZ DE FORA":"ChIJoV344UOcmAARaKSgsyawNmI",
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

def add_row():
    row_frame = Frame(data_frame)
    row_frame.pack(fill='x', pady=5)

    # Label para o ponto de entrega
    delivery_label = Label(row_frame, text="Ponto de Entrega:")
    delivery_label.pack(side='left', padx=5)

    # Menu suspenso para o ponto de entrega
    delivery_point_var = StringVar(row_frame)
    delivery_point_var.set(list(delivery_points_dict.keys())[0])  
    delivery_point_menu = OptionMenu(row_frame, delivery_point_var, *delivery_points_dict.keys())
    delivery_point_menu.pack(side='left', padx=5)

    # Label para a carga 
    load_label = Label(row_frame, text="Carga -")
    load_label.pack(side='left', padx=5)
    
    # Label para a carga - P
    load_label = Label(row_frame, text="P:")
    load_label.pack(side='left', padx=5)

    # Campo de texto para a carga - P
    load_P = Entry(row_frame, width=5)
    load_P.pack(side='left', padx=5)
    
    # Label para a carga - M
    load_label = Label(row_frame, text="M:")
    load_label.pack(side='left', padx=5)

    # Campo de texto para a carga - M
    load_M = Entry(row_frame, width=5)
    load_M.pack(side='left', padx=5)
    
    # Label para a carga - G
    load_label = Label(row_frame, text="G:")
    load_label.pack(side='left', padx=5)

    # Campo de texto para a carga - G
    load_G = Entry(row_frame, width=5)
    load_G.pack(side='left', padx=5)

    # Armazena a nova linha
    data_rows.append((delivery_point_var, load_P, load_M, load_G))

def get_distance_matrix():
    
    ids_list = []
    
    for row in data_rows:
        delivery_point_var, load_P, load_M, load_G = row
    
        # Acessa o valor da StringVar usando .get()
        delivery_point = delivery_point_var.get()
        
        # Verifica se o valor está no dicionário
        if delivery_point in delivery_points_dict:
            ids_list.append("place_id:"+delivery_points_dict[delivery_point])
        else:
            print(f"Ponto de entrega '{delivery_point}' não encontrado no dicionário.")

    for delivery_id in ids_list:
        dist_matrix = mp.build_url(delivery_id, ids_list)  # Passa o ID e a lista completa
        print(dist_matrix)

if __name__ == '__main__':
    window = Tk()
    window.title("Gerador de Rotas de Entrega")
    window.config(padx=50, pady=50)

    data_frame = Frame(window)
    data_frame.pack(fill='both', expand=True)

    data_rows = []
    add_row()

    button_frame = Frame(window)
    button_frame.pack(side='bottom', fill='x', pady=10)

    add_row_button = Button(button_frame, text="+", width=5, command=add_row)
    add_row_button.pack(side='left', padx=5)

    create_button = Button(button_frame, text="Gerar rotas", width=36, command=get_distance_matrix)
    create_button.pack(side='right', padx=5)

    window.mainloop()