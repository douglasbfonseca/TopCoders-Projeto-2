def busca_e():
    ...
def busca_ou():
    ...

def buscar_musicos():
    parametros_busca = input()
    tipo_busca = input("Para uma busca restrita digite 'e', caso contrário a busca será ampla").lower()
    busca_e() if tipo_busca == "e" else busca_ou()