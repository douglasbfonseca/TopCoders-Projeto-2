import json
from textwrap import indent

def busca_e(dict_busca:dict[tuple]):
    print(f"\nBusca tipo E para:\n{dict_busca}\n")

    try:
        with open("Projeto_2/cadastro_musicos.json", "r", encoding="utf8") as arquivo:
            cadastro_geral = json.load(arquivo)
    except:
        print("Não foi possível abrir o arquivo.")
    
    lista_e = []
    for musico in cadastro_geral:
        soma = 0
        for chave_busca in dict_busca:
            if dict_busca[chave_busca] == musico[chave_busca]:
                soma += 1
            elif dict_busca[chave_busca] in musico[chave_busca]:
                soma += 1
        if soma == len(dict_busca):
            lista_e.append(musico)

    return lista_e
def busca_ou(dict_busca:dict[tuple]) -> list[dict]:
    print(f"\nBusca tipo OU para:\n{dict_busca}\n")

    try:
        with open("Projeto_2/cadastro_musicos.json", "r", encoding="utf8") as arquivo:
            cadastro_geral = json.load(arquivo)
    except:
        print("Não foi possível abrir o arquivo.")

    lista_ou = []
    lista_de_emails = []
    for elemento_busca in dict_busca:

        if elemento_busca == 'nome' or elemento_busca == 'email':
            for musico in cadastro_geral:
                if (dict_busca[elemento_busca] in musico.values()) and (musico['email'] not in lista_de_emails):
                    lista_ou.append(musico)
                    lista_de_emails.append(musico['email'])
        else:
            for musico in cadastro_geral:
                if (dict_busca[elemento_busca] in musico['genero'] or dict_busca[elemento_busca] in musico['instrumento']) and (musico['email'] not in lista_de_emails):
                    lista_ou.append(musico)
                    lista_de_emails.append(musico['email'])
    
    return lista_ou
def coletar_busca_do_usuario() -> dict:
    opcoes_busca = ['1-nome', '2-email', '3-genero', '4-instrumento']
    try:
        numero_parametros_busca = int(input("\nDigite quantos parametros deseja usar na busca(1-4):"))
        dict_busca = {}

        for i in range(numero_parametros_busca):
            parametro_busca = int(input(f"\nQual parâmetro buscar?{opcoes_busca}\nDigite somente um numero inteiro:"))

            chave_busca = opcoes_busca.pop(parametro_busca-1)
            opcoes_busca.insert(parametro_busca-1, str(parametro_busca)+"-já buscado")

            busca_usuario = input(f"\nDigite sua busca({chave_busca}):").lower()
            if chave_busca[2:] == "já buscado":
                print("Só é possível buscar 1 parâmetro por tipo!")
                raise Exception

            dict_busca[chave_busca[2:]] = busca_usuario

        return dict_busca
    except:
        print("Entrada inválida!")

def buscar_musicos():
    dict_busca = coletar_busca_do_usuario()
    
    tipo_busca = input("\nPara uma busca restrita(tipo e) digite 'e', caso contrário a busca será ampla (tipo ou)").lower()
    resultado_busca = busca_e(dict_busca) if tipo_busca == "e" else busca_ou(dict_busca)
    
    if resultado_busca == []:
        return print("Não houve resultado para esta busca.")
    else:
        return resultado_busca

print(buscar_musicos())