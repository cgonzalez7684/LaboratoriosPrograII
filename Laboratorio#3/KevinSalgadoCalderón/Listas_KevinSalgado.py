# Una lista con las edades de los alumnos de la clase

edades = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
print(edades) #Imprimir la lista

print(edades[1]) #Acceder a un elemento de la lista

edades.append(31) #Añadir un elemento a la lista
print("Despues del append: ", edades)

edades[0] = "17" # type: ignore #Cambiar un elemento de la lista

del edades[8] #Eliminar un elemento de la lista

for edad in edades: #Recorrer la lista
    print(edad)



