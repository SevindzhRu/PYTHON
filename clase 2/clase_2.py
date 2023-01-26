lista = ["Seva", "Shukurova", 36, 1986]

# print(f"Mi nombre es: {lista[0]}.\nMi apellido es: {lista[1]}")

# lista = [1,2,3,4]
# lista.pop(2)
# print(lista)
# lista.remove (2)
# print(lista)

lista = ["a", "z", "c", "b"]
lista.sort()
# print(lista)
lista.reverse()
# print(lista, "metodo reverse")

lista_2 = [18, 20, 123, 5, 2, 4]
# lista_2.remove(5)
lista_2.pop(5)
# print(lista_2)

# lista_0 = [1, 2, 3, 4]
# lista_0.append(5)
# lista_0.count(1)
# print(lista_0, "lista")
# tupla_0 = (1, 2, 3, 4)
# tupla_0.count(1)
# print(tupla_0.index(4))

diccionario = {
    "Nombre": "Seva",
    "Edad": 36,
    "DNI": 123456,
    "Celular": 987654
}
# print(diccionario.items())
print(id(diccionario))
# diccionario.clear()
dic_2 = diccionario.copy()
print(id(dic_2))




