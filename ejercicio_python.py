'''

Haga un algoritmo que solicite la cantidad de frutas de cada tipo que hay en un supermercado, se debe solicitar a un usuario que ingrese el tipo de fruta y su cantidad.

Haga un menu que realice lo siguiente:

1. Calcule la cantidad total de frutas registradas
2. Imprima la cantidad de frutas de cada tipo
3. Imprima los tipos de fruta
4. Imprima el numero total de frutas del supermercado

'''
menu_frutas = "\nMENU FRUTAS\n\n"
menu_frutas += "1. Registrar frutas\n"
menu_frutas += "2. Consultar cantidad de frutas por tipo\n"
menu_frutas += "3. Consultar tipo de frutas registradas\n"
menu_frutas += "4. Consultar total de frutas del supermercado\n"
menu_frutas += "5. Consultar registro completo de inventario de frutas y cantidad\n"
menu_frutas += "6. Actualizar cantidad de frutas por tipo\n"
menu_frutas += "7. Eliminar frutas\n"
menu_frutas += "8. Salir\n"
menu_frutas += "Opcion: "

diccionario_frutas = {}

codigo = 0

while(codigo!= 8):
    suma = 0
    codigo=int(input(menu_frutas))

    if(codigo == 1):
        solicita_ingreso = "si"

        while(solicita_ingreso == "si"):
            nombre = input("Ingrese la fruta: ").lower()
            cantidad = int(input(f"Ingrese la cantidad correspondiente a la fruta {nombre}: "))

            diccionario_frutas[nombre]=cantidad
            print()
            print(diccionario_frutas)
            solicita_ingreso = input("\nDesea ingresar otra fruta? (si) (no): ").lower()
            print()

    elif(codigo == 2):
        print("\nCantidad de frutas por tipo")
        tipo_fruta=input("Ingrese la fruta a consultar: ").lower()

        if(tipo_fruta in diccionario_frutas):
            print(f"{tipo_fruta} - {diccionario_frutas.get(tipo_fruta)}")
        else:
            print(f"La fruta {tipo_fruta} no se encuentra en bodega")

    elif(codigo == 3):
        print("\nTipos de frutas:")
        for clave in diccionario_frutas:
            print(clave)

    elif(codigo == 4):
        for clave in diccionario_frutas:
            suma += diccionario_frutas.get(clave)
        
        print(f"\nLa cantidad de frutas es: {suma}")

    elif(codigo == 5):
        print("\nRegistro total de frutas y cantidad: ")
        for clave in diccionario_frutas:
            print(f"{clave} - {diccionario_frutas.get(clave)}")

    elif(codigo == 6):
        print("\nActualizar frutas")
        tipo_fruta = input("Ingrese la fruta a actualizar: ").lower()
        if(tipo_fruta in diccionario_frutas):
            cantidad = int(input(f"Ingrese la cantidad de la fruta {tipo_fruta}: "))
            diccionario_frutas[tipo_fruta] = cantidad
            print(f"{tipo_fruta} - {diccionario_frutas.get(tipo_fruta)}")
        else:
            print(f"La fruta {tipo_fruta} no esta registrada")
            
    
    elif(codigo == 7):
        print("\nEliminar frutas")
        tipo_fruta = input("Ingrese la fruta que desea eliminar: ").lower()
        if(tipo_fruta in diccionario_frutas):
            diccionario_frutas.pop(tipo_fruta)
            print("Fruta eliminada")
        else:
            print(f"La fruta {tipo_fruta} no esta registrada")
            
print("Salio!")