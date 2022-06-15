# from logging import exception


# email = "a aa!"

# soma = 0
# for caractere in email:
#     if caractere == "@":
#         soma += 1
#         continue
#     elif caractere.isdigit() or caractere.isalpha() or caractere == "_" or caractere == ".":
#         pass
#     else:
#         print("E-mail deve conter apenas letras, '_', '.', números e exatamente 1 '@'")
#         raise Exception
# if not (soma == 1):
#     raise Exception
dic1 = {"a":"aa"}
dic2 = {"a":"ab"}
dic3 = {"a":"abc"}

lista = [dic1, dic2, dic3]

for dic in lista:
    if "abc" in dic.values():
        print("entrou")
