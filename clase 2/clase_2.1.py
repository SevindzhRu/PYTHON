lista = [1, 2, 3, 4, 4, 5, 6, 9]
tupla = tuple(lista)
conjunto = set(lista)
# print(lista)
# print(tupla)
# print(conjunto)
conjunto.add(19)
lista_2 = [56, 59, 60]
conjunto.add(lista_2[0])
conjunto.add(lista_2[1])
conjunto.add(lista_2[2])
# print(conjunto)
lista_3 = [4]
tupla_2 = (1, 2, 3, lista_3)
# print(tupla_2)
# lista_3.append(5)
# print(tupla_2)
# lista_3[0] = 0
# print(lista_3)
# tupla_2[0] = 2

tupla = (1, 3, 2, 3)
print((set(tupla)))
cadena = "122345"
lista_6 = list(cadena)
print(cadena, lista_6)