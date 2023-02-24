# Creamos una lista vacía para empezar
mi_lista = []

# Función para imprimir la lista
def imprimir_lista():
    print("Paises agregados a la lista:")
    print(" ")
    for elemento in mi_lista:
        print(elemento)

# Menú principal del programa
print("El siguiente sistema te muestra cómo agregar, eliminar, modificar, recorrer y salir de una lista de 'Paises', por favor ") 
print(" ")

try: 
    while True:
        
        
        print("Seleccione una opción:")
        print("1. Agregar Pais")
        print("2. Eliminar Pais")
        print("3. Modificar Pais")
        print("4. Recorrer lista")
        print("5. Salir")
        print(" ")
        
        # Pedimos la opción al usuario
        opcion = int(input("Opción seleccionada: "))
        print(" ")
        
        # Acciones según la opción seleccionada #Contexto Agregamos, eliminamos, modificamos y recurremos nuestra lista de Paises
        
        if opcion == 1:
            elemento = input("Ingrese el Pais a agregar: ")
            print(" ")
            mi_lista.append(elemento)
            print("Pais agregado exitosamente.")
            print(" ")
        elif opcion == 2:
            if len(mi_lista) == 0:
                print("La lista está vacía.")
                print(" ")
            else:
                elemento = input("Ingrese el Pais a eliminar: ")
                print(" ")
                if elemento in mi_lista:
                    mi_lista.remove(elemento)
                    print("Pais eliminado exitosamente.")
                    print(" ")
                else:
                    print("El Pais no se encuentra en la lista.")
                    print(" ")
        elif opcion == 3:
            if len(mi_lista) == 0:
                print("La lista está vacía.")
                print(" ")
            else:
                elemento_viejo = input("Ingrese el Pais a modificar: ")
                print(" ")
                if elemento_viejo in mi_lista:
                    indice = mi_lista.index(elemento_viejo)
                    elemento_nuevo = input("Ingrese el nuevo Pais a agregar: ")
                    print(" ")
                    mi_lista[indice] = elemento_nuevo
                    print("Pais modificado exitosamente.")
                    print(" ")
                else:
                    print("El Pais no se encuentra en la lista.")
                    print(" ")
        elif opcion == 4:
            if len(mi_lista) == 0:
                print("La lista está vacía.")
                print(" ")
            else:
                imprimir_lista()
        elif opcion == 5:
            print("¡Hasta luego!")
            print(" ")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            print(" ")
#coloco un try except porque si el usuario se equivoca y en vez de un valor int coloca una letra u otro valor que no sea entero, el sistema no se rompa
#en dado caso si se cae, el sistema le muestre un mensaje mas apropiado al usuario
except:
 print(" OOOO :( , seleccione una opción válida") 