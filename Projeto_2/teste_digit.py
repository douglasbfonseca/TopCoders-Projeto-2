teste = [('daniel@gmail.com', 'baterista'), ('ana@gmail.com', 'guitarra'), ('daniel@gmail.com', 'vocal'), ('jorge@gmail.com', 'baterista'), ['paula@gmail.com', 'guitarra']]
instrumentos = ['guitarra','baterista','vocal']

def filtrador(instrumento):
    def item_filtrador(lista_musicos):
        return lista_musicos[1] == instrumento
    return item_filtrador

print(teste)
print()

musicos = []
for item in instrumentos:
    musicos.append(list(filter(filtrador(item),teste)))

print(musicos)
print()


def gera_bandas(colecao, banda = [], combinacoes = []):

    instrumento = colecao.pop()
    for musico in instrumento:
        if musico in banda:
            continue

        banda.append(musico)
        if colecao:
            combinacoes = gera_bandas(colecao, banda, combinacoes)
        else:
            combinacoes.append(banda.copy())
        banda.pop()
    colecao.append(instrumento)
    return combinacoes

combinacoes_banda = gera_bandas(musicos)

print(musicos)
print()
print(combinacoes_banda)
        