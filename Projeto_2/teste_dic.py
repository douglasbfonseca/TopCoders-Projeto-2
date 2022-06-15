import json
from textwrap import indent

def castrar_1_musico() -> dict:
    musico = dict()
    musico['nome']  = input("Insira o nome do músico:").lower()
    musico['email'] = input("Insira o e-mail do músico:").lower()
    
    resposta = ""
    lista_generos = []
    while resposta != "proximo":
        resposta = input("Insira o(s) gênero(s) do músico:(digite 'proximo' para não cadastrar)\n").lower()
        lista_generos.append(resposta)
    musico['genero'] = lista_generos

    resposta = ""
    lista_instrumentos = []
    while resposta != "proximo":
        resposta = input("Insira o(s) instrumento(s) do músico:(digite 'proximo' para não cadastrar)\n").lower()
        lista_instrumentos.append(resposta)
    musico['instrumento'] = lista_instrumentos

    return musico

def cadastrar_musicos():
    try:
        with open("Projeto_2/cadastro_musicos.json", "r", encoding="utf8") as arquivo:
            cadastro_geral = json.load(arquivo)
    except:
        print("Não há cadastro, iremos começar um novo!")
    
    cadastro_geral.append(castrar_1_musico())

    with open("Projeto_2/cadastro_musicos.json", "w", encoding="utf8") as arquivo:
         arquivo.write(json.dumps(cadastro_geral, indent=4))

cadastrar_musicos()