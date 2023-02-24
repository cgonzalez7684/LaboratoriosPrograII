# Definimos la lista inicial
nombres = ['Alberto', 'Daniel', 'Gerardo','Jordan']

while True:
    # Mostramos el menú de opciones
    print('\n¿Qué acción deseas realizar?\n')
    print('1. Agregar un nombre')
    print('2. Eliminar un nombre')
    print('3. Modificar un nombre')
    print('4. Recorrer la lista')
    print('5. Salir')
    
    # Solicitamos al usuario que seleccione una opción
    opcion = int(input('\nIngresa el número de la opción que deseas: '))
    
    if opcion == 1:
        # Si el usuario selecciona la opción 1, pedimos el nombre que desea agregar y lo agregamos a la lista
        nombre = input('Ingresa el nombre que deseas agregar: ')
        nombres.append(nombre)
        print(f'\nEl nombre {nombre} ha sido agregado a la lista.\n')
    elif opcion == 2:
        # Si el usuario selecciona la opción 2, pedimos el índice del nombre que desea eliminar y lo eliminamos de la lista
        indice = int(input('Ingresa el índice del nombre que deseas eliminar: '))
        nombre_eliminado = nombres.pop(indice)
        print(f'\nEl nombre {nombre_eliminado} ha sido eliminado de la lista.\n')
    elif opcion == 3:
        # Si el usuario selecciona la opción 3, pedimos el índice del nombre que desea modificar y el nuevo nombre
        indice = int(input('Ingresa el índice del nombre que deseas modificar: '))
        nuevo_nombre = input('Ingresa el nuevo nombre: ')
        nombres[indice] = nuevo_nombre
        print(f'\nEl nombre en el índice {indice} ha sido cambiado a {nuevo_nombre}.\n')
    elif opcion == 4:
        # Si el usuario selecciona la opción 4, recorremos la lista y mostramos cada nombre
        print('\nLos nombres en la lista son:\n')
        for nombre in nombres:
            print(nombre)
    elif opcion == 5:
        # Si el usuario selecciona la opción 5, salimos del programa
        print('\n¡Hasta luego!')
        break
    else:
        # Si el usuario ingresa una opción inválida, mostramos un mensaje de error
        print('\nLa opción ingresada es inválida. Por favor, intenta de nuevo.\n')
