import json
import re
from textwrap import indent

def abridor_modo_ler() -> list[dict]:
    with open("Projeto_2/cadastro_musicos.json", "r", encoding="utf8") as arquivo:
            cadastro_geral = json.load(arquivo)
    return cadastro_geral
def atualizador(cadastro_geral:list[dict])-> None:
    with open("Projeto_2/cadastro_musicos.json", "w", encoding="utf8") as arquivo:
         arquivo.write(json.dumps(cadastro_geral, indent=4))

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
        cadastro_geral = abridor_modo_ler()
    except:
        print("Não há cadastro, iremos começar um novo!")
    
    novo_musico = cadastrar_1_musico()
    
    if (novo_musico != None):
        for musico in cadastro_geral:
            if novo_musico['email'] in musico.values():
                print("\nEsse e-mail já está cadastrado, tente novamente.")
                raise Exception
        cadastro_geral.append(novo_musico)

    atualizador(cadastro_geral)

def busca_e(dict_busca:dict[str]) -> list[dict]:
    print(f"\nBusca tipo E para:\n{dict_busca}\n")

    try:
        with open("Projeto_2/cadastro_musicos.json", "r", encoding="utf8") as arquivo:
            cadastro_geral = json.load(arquivo)
    except:
        print("Não foi possível abrir o arquivo.")
        return None
    
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
def busca_ou(dict_busca:dict[str]) -> list[dict]:
    print(f"\nBusca tipo OU para:\n{dict_busca}\n")

    try:
        with open("Projeto_2/cadastro_musicos.json", "r", encoding="utf8") as arquivo:
            cadastro_geral = json.load(arquivo)
    except:
        print("Não foi possível abrir o arquivo.")
        return None

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
    except:
        print("Entrada inválida!")
    
    tipo_busca = input("\nPara uma busca restrita(tipo E) digite 'e', caso contrário a busca será ampla (tipo OU): ").lower()
    resultado_busca = busca_e(dict_busca) if tipo_busca == "e" else busca_ou(dict_busca)
    
    if resultado_busca == [] or resultado_busca == None:
        return print("Não houve resultado para esta busca.")
    else:
        return print(resultado_busca)

def modificador(email_musico, genero_ou_instrumento, add_ou_remover):
    try:
        # with open("Projeto_2/cadastro_musicos.json", "r", encoding="utf8") as arquivo:
        #     cadastro_geral = json.load(arquivo)
        cadastro_geral = abridor_modo_ler()
    except:
        print("Não foi possível abrir o arquivo.")

    if add_ou_remover == "adicionar":
        for musico in cadastro_geral:
            if musico['email'] == email_musico:
                print(f"\nQual {genero_ou_instrumento} deseja {add_ou_remover}?")
                print(musico[genero_ou_instrumento])
                musico[genero_ou_instrumento].append(input())
                print("adição com sucesso")
                print(musico[genero_ou_instrumento])
    else:
        for musico in cadastro_geral:
            if musico['email'] == email_musico:
                print(f"\nQual {genero_ou_instrumento} deseja {add_ou_remover}?")
                print(musico[genero_ou_instrumento])
                try:
                    musico[genero_ou_instrumento].pop(musico[genero_ou_instrumento].index(input()))
                    print("remoção com sucesso")
                    print(musico[genero_ou_instrumento])
                except:
                    print(f"Não é possível remover este {genero_ou_instrumento} pois ele não está cadastrado!")
    
    atualizador(cadastro_geral)
def modificar_musicos():      
    email_musico = input("\nDigite o e-mail do músico que deseja modificar:")
    
    genero_ou_instrumento = ""
    while genero_ou_instrumento != "genero" and genero_ou_instrumento != "instrumento":
        genero_ou_instrumento = input("\nDeseja modificar um gênero ou um instrumento?(GENERO/INSTRUMENTO)").lower()
    add_ou_remover = ""
    while add_ou_remover != "adicionar" and add_ou_remover != "remover":
        add_ou_remover = input(f"\nDeseja adicionar ou remover o {genero_ou_instrumento}?(ADICIONAR/REMOVER)").lower()

    modificador(email_musico, genero_ou_instrumento, add_ou_remover)

def multiplica_lista(numero_instrumentos):
    multiplicacao = 1
    for i in numero_instrumentos:
        multiplicacao *= i
    return multiplicacao
def contador_bandas(lista_tuplas,instrumentos_banda):
    lista_numerica_instr_banda = []
    for instrumento in instrumentos_banda:
        soma = 0
        for tupla in lista_tuplas:
            if instrumento == tupla[1]:
                soma +=1
        lista_numerica_instr_banda.append(soma)
    return multiplica_lista(lista_numerica_instr_banda)

    ...
def verificador_bandas(lista_bandas:list[list[tuple]],tupla:tuple)->bool:
    if lista_bandas == []:
        return True
    
    for banda in lista_bandas:
        for musico in banda:
            if musico[0] == tupla[0]:
                return False
            elif musico[1] == tupla[1]:
                return False
    return True
    ...
def iterador_de_bandas(lista_tuplas,instrumentos_banda) -> list[tuple]:
    
    verificacao = verificador_bandas
    numero_max_bandas = contador_bandas(lista_tuplas,instrumentos_banda)
    lista_bandas = []
    banda = []
    
    for i in range(numero_max_bandas):
        for tupla in lista_tuplas:
            if verificacao(lista_bandas,instrumentos_banda):
                banda.append(tupla)
            if len(banda) == len(instrumentos_banda):
                lista_bandas.append(banda)
                banda = []
                break
    return lista_bandas
def criar_tuplas(aptos_para_banda, instrumentos_banda) -> list[tuple]:
    lista_tuplas_com_repeticao = []
    for lista in aptos_para_banda:
        for musico in lista:
            for instrumento in musico['instrumento']:
                if instrumento in instrumentos_banda:
                    lista_tuplas_com_repeticao.append((musico['email'],instrumento))
    
    lista_tuplas = []
    for tupla in lista_tuplas_com_repeticao:
        if tupla not in lista_tuplas:
            lista_tuplas.append(tupla)
    
    #Não entendi pq essa list comprehension não funciona??!!
    #lista_tuplas = [tupla for tupla in lista_tuplas_com_repeticao if tupla not in lista_tuplas]
    
    return lista_tuplas
def montar_bandas():
    genero_banda = input("\nQual o gênero da sua banda?")
    try:
        tamanho_banda = int(input("\nQuantos músicos tocarão na banda?"))
    except ValueError:
        return print("Erro, o número de músicos deve ser um inteiro.")
    
    instrumentos_banda = [input(f"\nDigite o instrumento de número {i+1}: ") for i in range(tamanho_banda)]
    aptos_para_banda = [busca_e({'genero':genero_banda, 'instrumento':instr}) for instr in instrumentos_banda]
    lista_tuplas = criar_tuplas(aptos_para_banda, instrumentos_banda)
    lista_bandas = iterador_de_bandas(lista_tuplas, instrumentos_banda)
    print(lista_bandas)

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