
autos_lista = []

# Para agregar se utiliza append c/u o extend para varios
autos_lista.extend(["BMW","Mercedes-Benz","Ford","Toyota","Nissan","Kia"])
# autos_lista.append("Mercedes-Benz")
# autos_lista.append("Ford")
# autos_lista.append("Toyota")
# autos_lista.append("Nissan")
# autos_lista.append("Kia")
print("Mi lista de autos es:", autos_lista)

print("***************************")
# Para modificar se utiliza el indice
autos_lista[2] = "Ferrari"
print("Lista modificada de autos es:", autos_lista)

print("***************************")
# Para eliminar se utiliza el valor
autos_lista.remove("Toyota")
print("Lista con elemento eliminado:", autos_lista)

print("***************************")
# Se puede eliminar el ultimo elemento con pop
ultimo_elemento = autos_lista.pop()
print("El último auto de la lista es:", ultimo_elemento)
print("Lista de autos despues de eliminar el ultimo:", autos_lista)

print("***************************")
# Para recorrer lista se utiliza for
print("Los elementos de la lista de autos son:")
for elemento in autos_lista:
    print(elemento)