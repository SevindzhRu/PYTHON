menu = {
    1: "Agregar contacto",
    2: "Eliminar contacto",
    3: "Editar contacto",
    4: "Ver todos los contactos",
    5: "Busca todos los contactos",
    6: "Salir"
}

contactos = {}

def mostrar_diccionario(diccionario: dict):
 for x,y in diccionario.items():
    print(f"{x}. {y}")

def comprobar_opcion(opcion):
    if opcion >=1 and opcion <=6:
        # print("\nopcion correcta")
        if opcion == 1:
            agregar_contacto()
            return True
        elif opcion == 2:
            eliminar_contacto()
            return True
        elif opcion == 6:
            return False

        return True
    else:
        print("\nOpcion incorrecta, por favor elija del 1 al 6")
        return True

# mostrar_diccionario(menu)

def agregar_contacto():
    nombre = input("Ingrese el nombre de contacto: ")
    id = input("Ingrese el ID: ")
    direccion = input("Ingrese la direccion de contacto: ")
    celular = input("Ingrese el celular de contacto: ")

    contactos[nombre] = {"ID": id, "Direccion": direccion, "Celular": celular}
    print("Contacto guardado")

def eliminar_contacto():
    nombre = input("Ingrese el nombre de contacto que quiere eliminar: ")
    contactos.pop(nombre)
    print(f"Contacto {nombre} eliminado")

verificacion = True

while verificacion:
    mostrar_diccionario(menu)
    valor = int(input("\nElija una opcion: "))
    verificacion = comprobar_opcion(valor)

print(contactos)

