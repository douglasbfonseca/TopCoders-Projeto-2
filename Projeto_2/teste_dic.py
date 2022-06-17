
import json
from textwrap import indent



def modificador(email_musico, genero_ou_instrumento, add_ou_remover):
    try:
        with open("Projeto_2/cadastro_musicos.json", "r", encoding="utf8") as arquivo:
            cadastro_geral = json.load(arquivo)
        #cadastro_geral = abridor_modo_ler()
    except:
        print("Não foi possível abrir o arquivo.")

    if add_ou_remover == "adicionar":
        for musico in cadastro_geral:
            if musico['email'] == email_musico:
                print(f"\nQual {genero_ou_instrumento} deseja {add_ou_remover}?")
                print(musico[genero_ou_instrumento])
                musico[genero_ou_instrumento].append(input())
                return musico
    else:
        for musico in cadastro_geral:
            if musico['email'] == email_musico:
                print(f"\nQual {genero_ou_instrumento} deseja {add_ou_remover}?")
                print(musico[genero_ou_instrumento])
                try:
                    musico[genero_ou_instrumento].pop(musico[genero_ou_instrumento].index(input()))
                except:
                    print(f"Não é possível remover este {genero_ou_instrumento} pois ele não está cadastrado!")

def modificar_musicos():      
    email_musico = input("\nDigite o e-mail do músico que deseja modificar:")
    
    genero_ou_instrumento = ""
    while genero_ou_instrumento != "genero" and genero_ou_instrumento != "instrumento":
        genero_ou_instrumento = input("\nDeseja modificar um gênero ou um instrumento?(GENERO/INSTRUMENTO)").lower()
    add_ou_remover = ""
    while add_ou_remover != "adicionar" and add_ou_remover != "remover":
        add_ou_remover = input(f"\nDeseja adicionar ou remover o {genero_ou_instrumento}?(ADICIONAR/REMOVER)").lower()

    modificador(email_musico, genero_ou_instrumento, add_ou_remover)
    




