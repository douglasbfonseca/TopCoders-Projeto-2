def cadastrar_musicos ():
    ...
def buscar_musicos():
    ...
def modificar_musicos():
    ...
def montar_bandas():
    ...
def menu():
    opcao_usuario = input()
    opcoes = {
        "1": cadastrar_musicos(),
        "2": buscar_musicos(),
        "3": modificar_musicos(),
        "4": montar_bandas(),
    }

menu()