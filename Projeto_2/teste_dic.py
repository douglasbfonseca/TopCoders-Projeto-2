lista_de_bandas = []

def criador_obj(lista_de_bandas:list,numero_max_bandas):
    lista_vazia = []
    for i in range(numero_max_bandas):
        lista_de_bandas.append(lista_vazia)
    return lista_de_bandas    

def separar_por_instrumento(lista_tuplas,instrumentos_banda):
    lista_separada = []
    for instrumento in instrumentos_banda:
        lista_provisoria = []
        for tupla in lista_tuplas:
            if instrumento == tupla[1]:
                lista_provisoria.append(tupla)
        lista_separada.append(lista_provisoria)
    return lista_separada

def iterador(lista_de_bandas:list,lista_separada):
    for lista in lista_separada:
        for tupla in lista:
            for i in range()










