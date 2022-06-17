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
dic2 = {"b":"ab"}
dic3 = {"c":[1,2,3,4,5,6]}

dict_vazio = {}
dict_vazio["teste"] = "teste1"
dict_vazio["teste2"] = "teste12"
dict_vazio["teste3"] = "teste123"
print(len(dict_vazio))
# for i in dict_vazio:
#     print(i)
dic3["c"].pop(1)
print(dic3)