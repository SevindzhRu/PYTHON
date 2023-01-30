# nombre = input("Ingresa tu nombre:")
# edad = int(input("Que edad tienes: "))

# if edad >18:
#     print(f"{nombre} es mayor de edad")
# elif edad == 18:
#     print(f"La edad de {nombre} es 18")
# else:
#     print(f"{nombre} no es mayor de edad")


# numero_1 = 18
# numero_2 = 280

# if not numero_1 > 100 and numero_2 > 100:
#     print("Los numeros son mayores a 100")
# else:
#     print("Los numeros no son mayores a 100")

# lista = ["a", "b", "c", "d"]
# for elemento in lista:
#     print(elemento)

# diccionario = {
#     "nombre": "Seva",
#     "apellido": "Shukurova",
#     "direccion": "Calle Los Tucanes"
# }

# print(diccionario.items())

# for dato in diccionario.items():
#     print(dato)

# variable = 4
# print(variable < 10)

# while variable < 10:
#     print(variable)
#     print("Estoy en el ciclo while")
#     variable += 1
#     variable = variable + 1

# def funcion_suma(a, b):
#     resultado = a + b
#     print(resultado)

# funcion_suma(2, 3)
# funcion_suma("hola ", "mundo")

def funcion_multiplicar (valor_1, valor_2):
    return valor_1 * valor_2

print(funcion_multiplicar(5,3))
variable = funcion_multiplicar(2,3)
print(variable)

suma = lambda a,b : a + b
print(suma(2,3))
print((lambda a,b : a * b)(5,3))
