import email
import json
from textwrap import indent

def validador_entrada(musico):
    for caractere in musico['nome']:
        if caractere.isalpha() or caractere.isspace():
            pass
        else:
            print("\nO nome deve ser composto apenas de letras e espaços.")
            raise Exception
    
    soma = 0
    for caractere in musico['email']:
        if caractere == "@":
            soma += 1
            continue
        elif caractere.isdigit() or caractere.isalpha() or caractere == "_" or caractere == ".":
            pass
        else:
            print("\nE-mail deve conter apenas letras, '_', '.', números e exatamente 1 '@'")
            raise Exception
    if not (soma == 1):
        raise Exception

def cadastrar_1_musico() -> dict:
    musico = dict()
    musico['nome']  = input("Insira o nome do músico:").lower()
    musico['email'] = input("Insira o e-mail do músico:").lower()
    
    resposta = ""
    lista_generos = []
    while resposta != "proximo":
        resposta = input("Insira o(s) gênero(s) do músico:(digite 'proximo' para não cadastrar)\n").lower()
        lista_generos.append(resposta)
    musico['genero'] = lista_generos[:-1]

    resposta = ""
    lista_instrumentos = []
    while resposta != "proximo":
        resposta = input("Insira o(s) instrumento(s) do músico:(digite 'proximo' para não cadastrar)\n").lower()
        lista_instrumentos.append(resposta)
    musico['instrumento'] = lista_instrumentos[:-1]

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
        for elemento in cadastro_geral:
            if novo_musico['email'] in elemento.values():
                print("Esse e-mail já está cadastrado, tente novamente.")
                raise Exception
        cadastro_geral.append(cadastrar_1_musico())


    with open("Projeto_2/cadastro_musicos.json", "w", encoding="utf8") as arquivo:
         arquivo.write(json.dumps(cadastro_geral, indent=4))

def buscar_musicos():
    ...
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
        print("Bem vindo ao programa de formação de bandas, escolha uma opção:")
        print("1 - Cadastrar Músicos\n2 - Buscar Músicos\n3 - Modificar Músicos\n4 - Montar Bandas\n0 - Sair")
        opcao_usuario = input()
        try:
            opcoes[opcao_usuario]()
        except:
            print("Infelizmente ocorreu este erro!!!!")

menu()