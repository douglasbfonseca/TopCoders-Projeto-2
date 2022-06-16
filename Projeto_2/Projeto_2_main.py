import json
from textwrap import indent

def validador_entrada(musico):
    for caractere in musico['nome']:
        if caractere.isalpha() or caractere.isspace():
            continue
        else:
            print("\nO nome deve ser composto apenas de letras e espaços.")
            raise Exception
    
    soma = 0
    for caractere in musico['email']:
        if caractere == "@":
            soma += 1
            continue
        elif caractere.isdigit() or caractere.isalpha() or caractere == "_" or caractere == ".":
            continue
        else:
            print("\nE-mail deve conter apenas letras, '_', '.', números e exatamente 1 '@'")
            raise Exception
    if not (soma == 1):
        print("O e-mail deve conter exatamente 1 '@'")
        raise Exception
def cadastrar_1_musico() -> dict:
    musico = dict()
    musico['nome']  = input("Insira o nome do músico:").lower()
    musico['email'] = input("Insira o e-mail do músico:").lower()
    
    try:
        numero_genero = int(input("Insira numero de gênero(s) do músico:"))
    except ValueError:
        print("Erro, o número de gêneros deve ser um inteiro.")
    lista_generos = []
    for i in range(numero_genero):
        resposta = input("Insira um gênero do músico:").lower()
        lista_generos.append(resposta)
    musico['genero'] = lista_generos

    try:
        numero_instrumento = int(input("Insira numero de instrumento(s) do músico:"))
    except ValueError:
        print("Erro, o número de instrumentos deve ser um inteiro.")
    lista_instrumentos = []
    for i in range(numero_instrumento):
        resposta = input("Insira um instrumento do músico:").lower()
        lista_instrumentos.append(resposta)
    musico['instrumento'] = lista_instrumentos
    
    try:
        validador_entrada(musico)
        return musico
    except:
        print("Tente cadastrar o músico novamente.\n")
def cadastrar_musicos():
    try:
        with open("Projeto_2/cadastro_musicos.json", "r", encoding="utf8") as arquivo:
            cadastro_geral = json.load(arquivo)
    except:
        print("Não há cadastro, iremos começar um novo!")
    
    novo_musico = cadastrar_1_musico()
    
    if (novo_musico != None):
        for musico in cadastro_geral:
            if novo_musico['email'] in musico.values():
                print("\nEsse e-mail já está cadastrado, tente novamente.")
                raise Exception
        cadastro_geral.append(novo_musico)


    with open("Projeto_2/cadastro_musicos.json", "w", encoding="utf8") as arquivo:
         arquivo.write(json.dumps(cadastro_geral, indent=4))

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
def buscar_musicos():
    try:
        dict_busca = coletar_busca_do_usuario()
        tipo_busca = input("\nPara uma busca restrita(tipo E) digite 'e', caso contrário a busca será ampla (tipo OU): ").lower()
        resultado_busca = busca_e(dict_busca) if tipo_busca == "e" else busca_ou(dict_busca)
    except:
        print("Entrada inválida!")
    
    if resultado_busca == [] or resultado_busca == None:
        return print("Não houve resultado para esta busca.")
    else:
        return print(resultado_busca)

def modificar_musicos():
    ...
def montar_bandas():
    ...

def menu():
    opcoes = {
        "1": cadastrar_musicos,
        "2": buscar_musicos,
        "3": modificar_musicos,
        "4": montar_bandas,
        "0": "Sair"
    }
    
    opcao_usuario = "xxx"
    while opcao_usuario != "0":
        print("\nBem vindo ao programa de formação de bandas, escolha uma opção:")
        print("1 - Cadastrar Músicos\n2 - Buscar Músicos\n3 - Modificar Músicos\n4 - Montar Bandas\n0 - Sair")
        opcao_usuario = input()
        try:
            opcoes[opcao_usuario]()
        except:
            print("Infelizmente ocorreu este erro =(")

menu()