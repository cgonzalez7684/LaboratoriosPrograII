#Laboratorio 3 de Maria Paula Corrales Cespedes

print("--------------------------------------------------------")
print("   Bienvenido al sistmea de inventario Patitos S.A")
print("--------------------------------------------------------")
print()

def mostrar_menu():
    print("1. Añadir un articulo")
    print("2. Eliminar un articulo")
    print("3. Modificar un articulo")
    print("4. Mostrar inventario")
    print("5. Salir")
    print()

def agregar_item(inventario):
    print()
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    precio = float(input("Ingrese el precio: "))
    inventario.append((producto, cantidad, precio))
    print("Item añadido al inventario.")
    print()

def eliminar_item(inventario):
    print()
    producto = input("Ingrese el producto a eliminar: ")
    for i, (name, _, _) in enumerate(inventario):
        if name == producto:
            del inventario[i]
            print("Producto eliminado con exito.")
            print()
            return
    print("Producto no fue encontrado en el inventario.")
    print()

def modificar_item(inventario):
    print()
    producto = input("Ingrese el producto a modificar: ")
    for i, (name, _, _) in enumerate(inventario):
        if name == producto:
            cantidad = int(input("Ingrese la nueva cantidad: "))
            precio = float(input("Ingrese el nuevo precio: "))
            inventario[i] = (producto, cantidad, precio)
            print("Producto modificado con exito.")
            print()
            return
    print("Producto no fue encontrado en el inventario.")
    print()

def recorrer_inventario(inventario):
    print()
    print("En inventario:")
    for i, (name, cantidad, precio) in enumerate(inventario, 1):
        print(f"{i}. {name}, {cantidad}, {precio:.2f}")

def main():
    inventario = []
    while True:
        mostrar_menu()
        opcion = input("Digite una opcion: ")
        if opcion == "1":
            agregar_item(inventario)
        elif opcion == "2":
            eliminar_item(inventario)
        elif opcion == "3":
            modificar_item(inventario)
        elif opcion == "4":
            recorrer_inventario(inventario)
            print()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Error, intentar nuevamente.")

if __name__ == '__main__':
    main()