milista=["manzana","uva","naranja","limon"]
print("la lista sin modificaciones ", milista)
milista.append("fresa")
print("ahora agregamos una fruta ", milista)
milista.remove("uva")
print("ahora eliminamos la uva ", milista)
milista[2]="banano"
print("ahora modificamos la lista y agregamos un banano ", milista)

indice = 0
print("ahora recorremos la lista con un bucle while")
while indice < len(milista):
    print(milista[indice])
    indice += 1