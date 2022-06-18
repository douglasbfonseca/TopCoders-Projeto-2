from Projeto_2.Projeto_2_main import busca_e

def criar_tuplas(aptos_para_banda) -> list[tuple]:
    lista_tuplas = []
    for lista in aptos_para_banda:
        for musico in lista:
            lista_tuplas.append((musico['email'],musico['instrumento']))

    return lista_tuplas


def montar_bandas():
    genero_banda = input("\nQual o gênero da sua banda?")
    try:
        tamanho_banda = int(input("\nQuantos músicos tocarão na banda?"))
    except ValueError:
        return print("Erro, o número de músicos deve ser um inteiro.")
    
    instrumentos_banda = [input(f"\nDigite o instrumento de número {i+1}: ") for i in range(tamanho_banda)]
    aptos_para_banda = [busca_e({'genero':genero_banda, 'instrumento':instr}) for instr in instrumentos_banda]
    lista_tuplas = criar_tuplas(aptos_para_banda)
    print(lista_tuplas)




