import json
import re
from textwrap import indent

def abridor_modo_ler() -> list[dict]:
    '''Abre o arquivo no modo leitura e retorna o cadastro geral do programa.'''
    with open("Projeto_2/cadastro_musicos.json", "r", encoding="utf8") as arquivo:
            cadastro_geral = json.load(arquivo)
    return cadastro_geral
def atualizador(cadastro_geral:list[dict])-> None:
    '''Recebe o cadastro geral com as alterações feitas pelo programa e reescreve o arquivo.'''
    with open("Projeto_2/cadastro_musicos.json", "w", encoding="utf8") as arquivo:
         arquivo.write(json.dumps(cadastro_geral, indent=4))

def validador_entrada(musico:dict) -> None:
    '''Valida o cadastro feito pelo usuário.'''
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
    '''Função executora do cadastro.'''
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
    '''Função principal do cadastro, que irá chamar as função executora e checar a validade do cadastro feito.'''
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
        print("\nCadastro realizado com sucesso!\n")

    atualizador(cadastro_geral)

def busca_e(dict_busca:dict[str]) -> list[dict]:
    '''Executa a busca do tipo E.'''

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
    '''Executa a busca do tipo OU.'''
    
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
def coletar_busca_do_usuario() -> dict[str]:
    '''Coleta as informações de busca inseridas pelo usuário.'''

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
    '''Principal função de busca, ela chama as funções auxiliares e retorna o resultado para o usuário.'''
    
    try:
        dict_busca = coletar_busca_do_usuario()
        tipo_busca = input("\nPara uma busca restrita(tipo E) digite 'E', caso contrário a busca será ampla (tipo OU): ").lower()
        resultado_busca = busca_e(dict_busca) if tipo_busca == "e" else busca_ou(dict_busca)
    except:
        print("Entrada inválida, tente novamente!")
    
    if resultado_busca == [] or resultado_busca == None:
        print("Não houve resultado para esta busca.")
    else:
        for musico in resultado_busca:
            print(musico,"\n")

def modificador(email_musico:str, genero_ou_instrumento:str, add_ou_remover:str) -> None:
    '''Função executora da modificação, que recebe as decisões do usuário vinda da função principal.'''
    try:
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
                break
        else:
            print("Músico não encontrado, verifique se o email está correto.")
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
                break
        else:
            print("Músico não encontrado, verifique se o email está correto.")
    
    atualizador(cadastro_geral)
def modificar_musicos():
    '''Função principal da modificação, nela o usuário irá decidir entre: 
    (gênero ou instrumento) ou  (adicionar ou remover).'''      
    
    email_musico = input("\nDigite o e-mail do músico que deseja modificar:")
    
    genero_ou_instrumento = ""
    while genero_ou_instrumento != "genero" and genero_ou_instrumento != "instrumento":
        genero_ou_instrumento = input("\nDeseja modificar um gênero ou um instrumento?(GENERO/INSTRUMENTO)").lower()
    add_ou_remover = ""
    while add_ou_remover != "adicionar" and add_ou_remover != "remover":
        add_ou_remover = input(f"\nDeseja adicionar ou remover o {genero_ou_instrumento}?(ADICIONAR/REMOVER)").lower()

    modificador(email_musico, genero_ou_instrumento, add_ou_remover)

def criador_de_filtros(instrumento:str):
    '''Cria funções que irão ajudar na organização dos musicos por instrumento'''

    def filtrador(musico_banda):
        return musico_banda[1] == instrumento
    return filtrador
def filtrar_tuplas(lista_tuplas:list[tuple],instrumentos_banda:list[str]) -> list[tuple]:
    '''Filtra as tuplas através do criador de filtros,
    criando uma lista onde os músicos são organizados por instrumento.'''
    
    tuplas_filtradas = []
    for instrumento in instrumentos_banda:
        tuplas_filtradas.append(list(filter(criador_de_filtros(instrumento),lista_tuplas)))
    return tuplas_filtradas
def iterador_de_bandas(tuplas_filtradas:list[tuple], banda = [], lista_bandas = []) -> list[list[tuple]]:
    '''Itera músico a músico a fim de formar todas a combinações de bandas possíveis,
    respeitando as restrições.'''

    musico_repetido = False
    instrumento = tuplas_filtradas.pop()
    for musico in instrumento:
        
        for musico_banda in banda:
            if musico[0] == musico_banda[0]:
                musico_repetido = True
        if musico_repetido:
            musico_repetido = False
            continue

        banda.append(musico)
        if tuplas_filtradas:
            lista_bandas = iterador_de_bandas(tuplas_filtradas, banda, lista_bandas)
        else:
            lista_bandas.append(banda.copy())
        banda.pop()
    tuplas_filtradas.append(instrumento)
    return lista_bandas
def organizar_bandas(lista_bandas:list[list[tuple]]) -> list[list[tuple]]:
    '''Ordena as bandas por instrumento.'''
    
    for banda in lista_bandas:
        banda.sort(key = lambda musico: musico[1])
    return lista_bandas
def criar_tuplas(aptos_para_banda:list[dict], instrumentos_banda:list[str]) -> list[tuple]:
    '''Cria tuplas (email, instrumento), que são os possíveis membros das bandas.'''

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
    '''Função principal, que chama as funções que montam as bandas,
    além de printar o resultado final.'''
    
    genero_banda = input("\nQual o gênero da sua banda?")
    try:
        tamanho_banda = int(input("\nQuantos músicos tocarão na banda?"))
    except ValueError:
        return print("Erro, o número de músicos deve ser um inteiro.")
    
    instrumentos_banda = [input(f"\nDigite o instrumento de número {i+1}: ") for i in range(tamanho_banda)]
    aptos_para_banda = [busca_e({'genero':genero_banda, 'instrumento':instrumento}) for instrumento in instrumentos_banda]
    lista_tuplas = criar_tuplas(aptos_para_banda, instrumentos_banda)
    tuplas_filtradas = filtrar_tuplas(lista_tuplas, instrumentos_banda)
    lista_bandas = iterador_de_bandas(tuplas_filtradas, lista_bandas = [])
    lista_bandas = organizar_bandas(lista_bandas)
    
    if lista_bandas == []:
        print("Não foi possível formar uma banda com este gênero e estes intrumentos. =(")
    for bandas in lista_bandas:
        print("\n",bandas)

def funcao_saida():
    print("Obrigado por usar o programa, até mais!")

def menu():
    '''Principal função do programa, que chama suas funcionalidades.'''

    opcoes = {
        "1": cadastrar_musicos,
        "2": buscar_musicos,
        "3": modificar_musicos,
        "4": montar_bandas,
        "0": funcao_saida
    }
    
    opcao_usuario = "x"
    while opcao_usuario != "0":
        print("\nBem vindo ao programa de formação de bandas, escolha uma opção:")
        print("1 - Cadastrar Músicos\n2 - Buscar Músicos\n3 - Modificar Músicos\n4 - Montar Bandas\n0 - Sair")
        opcao_usuario = input()
        try:
            opcoes[opcao_usuario]()
        except:
            print("Infelizmente ocorreu este erro =(")

menu()