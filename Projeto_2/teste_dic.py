import json
from textwrap import indent

def busca_e(lista_busca:list[tuple]):
    ...
def busca_ou(lista_busca:list[tuple]) -> list[dict]:
    print(f"\nBusca tipo OU para:\n{lista_busca}")

    try:
        with open("Projeto_2/cadastro_musicos.json", "r", encoding="utf8") as arquivo:
            cadastro_geral = json.load(arquivo)
    except:
        print("Não foi possível abrir o arquivo.")

    lista_ou = []
    lista_de_emails = []
    for elemento_busca in lista_busca:

        if elemento_busca[0] == 'nome' or elemento_busca[0] == 'email':
            for musico in cadastro_geral:
                if (elemento_busca[1] in musico.values()) and (musico['email'] not in lista_de_emails):
                    lista_ou.append(musico)
                    lista_de_emails.append(musico['email'])
        else:
            for musico in cadastro_geral:
                if (elemento_busca[1] in musico['genero'] or elemento_busca[1] in musico['instrumento']) and (musico['email'] not in lista_de_emails):
                    lista_ou.append(musico)
                    lista_de_emails.append(musico['email'])
    
    return lista_ou

def coletar_busca_do_usuario() -> list[tuple]:
    opcoes_busca = ['1-nome', '2-email', '3-genero', '4-instrumento']
    try:
        numero_parametros_busca = int(input("Digite quantos parametros deseja usar na busca(1-4):"))
        lista_busca = []

        for i in range(numero_parametros_busca):
            parametro_busca = int(input(f"Qual parâmetro buscar?{opcoes_busca}\nDigite somente um numero inteiro:"))

            chave_busca = opcoes_busca.pop(parametro_busca-1)
            opcoes_busca.insert(parametro_busca-1, str(parametro_busca)+"-já buscado")

            busca_usuario = input(f"Digite sua busca({chave_busca}):").lower()
            tupla_busca = (chave_busca[2:], busca_usuario)
            
            if tupla_busca[0] == "já buscado":
                print("Só é possível buscar 1 parâmetro por tipo!")
                raise Exception

            lista_busca.append(tupla_busca)

        return lista_busca
    except:
        print("Entrada inválida!")

def buscar_musicos():
    lista_busca = coletar_busca_do_usuario()
    tipo_busca = input("\nPara uma busca restrita(tipo e) digite 'e', caso contrário a busca será ampla (tipo ou)").lower()
    resultado_busca = busca_e(lista_busca) if tipo_busca == "e" else busca_ou(lista_busca)
    return resultado_busca

print(buscar_musicos())