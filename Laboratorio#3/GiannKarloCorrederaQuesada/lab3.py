Frutas = ["manzana", "guanabana", "banano"]                                    #inicializamos la lista

Frutas.append("uva")                                                           #agregamos varias frutas a la lista
Frutas.append("mango")     
Frutas.append("limon")     
Frutas.append("papaya")     

Frutas.remove("guanabana")                                                     #eliminamos una fruta

Frutas[2] = "piña"                                                             #cambiamos la fruta de la posicion 2

print(len(Frutas))                                                             #imprimimos la cantidad de elementos que hay dentro de la lista

for x in Frutas:
    print(x)                                                                    #imprimimos de uno en uno los elementos que hay dentro de la lista con un for 



