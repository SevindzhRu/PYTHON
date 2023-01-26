#Ejercicio 1
datos = ["nombre", "apellido", "edad", "anio_nacimimiento"]
print(datos)

datos_diccionario = {
    "nombre": "Seva",
    "apellido": "Shukurova",
    "edad": 36,
    "anio_nacimiento": 1986
}

conjunto = {" "}
conjunto.add(input("Hobby:"))
conjunto.add(input("Comida favorita:"))
conjunto.add(input("Pais de tus sueños:"))

print(conjunto)

#Ejercicio 2
alumno_1 = {
    "Lengua": 9,
    "Matemática": 7,
    "Informática": 7
}

alumno_2 = {
    "Lengua": 3,
    "Matemática": 4,
    "Informática": 5
}

alumno_3 = {
    "Lengua": 8,
    "Matemática": 8,
    "Informática": 10
}

alumno_4 = {
    "Lengua": 6,
    "Matemática": 8,
    "Informática": 2
}

alumnos = {

}
alumnos["alumno_1"] = alumno_1
alumnos["alumno_2"] = alumno_2
alumnos.update({"alumno_3": alumno_3})
alumnos.update({"alumno_4": alumno_4})

print(alumnos)

alumno_4.update ({"arte":10})
alumnos.pop ("alumno_2")

print(alumnos)

alumno_5 = {}
lengua = int(input("Nota obtenida en lengua:"))
matematica = int(input("Nota de matematica:"))
informatica = int(input("Nota de informatica:"))


print(f"El alumno_5 obtuvo las siguintes notas en el primer bimestre:\nLengua:{lengua}\nMatematica:{matematica}\nInformatica:{informatica}")



