# Dylan Castro Rodriguez
#Elabore un programa tipo consola que permita ejemplificar las acciones de agregar, 
#eliminar, modificar y recorrer una estructura tipo <list>, el contexto del desarrollo 
#queda a criterio del estudiante. 
 
# Tienda videojuegos GameCRC
productos = []

def agregar_producto():
    nombre = input('Ingrese el nombre del producto: ')
    productos.append(nombre)
    print('El producto ha sido agregado a la lista.')

def eliminar_producto():
    nombre = input('Ingrese el nombre del producto que desea eliminar: ')
    if nombre in productos:
        productos.remove(nombre)
        print('El producto ha sido eliminado de la lista.')
    else:
        print('El producto no se encuentra en la lista.')

def modificar_producto():
    nombre = input('Ingrese el nombre del producto que desea modificar: ')
    if nombre in productos:
        indice = productos.index(nombre)
        nuevo_nombre = input('Ingrese el nuevo nombre del producto: ')
        productos[indice] = nuevo_nombre
        print('El nombre del producto ha sido modificado.')
    else:
        print('El producto no se encuentra en la lista.')
def recorrer_productos():
    print('Lista de productos comprados:')
    for producto in productos:
        print(producto)

while True:
    print('Bienvenido a la tienda de videojuegos')
    print('1. Agregar producto')
    print('2. Eliminar producto')
    print('3. Modificar producto')
    print('4. Recorrer lista de productos')
    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        eliminar_producto()
    elif opcion == '3':
        modificar_producto()
    elif opcion == '4':
        recorrer_productos()
        break
    else:
        print('Opción inválida')
