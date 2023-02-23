
ListaP=["arroz","frijoles","azucar","carnes","verduras"]


ListaP.append("atún")
ListaP.append("careal")
ListaP.append("papas")
#append. es para agregar articulos a la lista 

ListaP.remove("azucar")
#remore se puede usar para borrar un solo elemento

ListaP[4] = "aceite"
#este sirve para modificar lo que se encuentre en la poccion dada

for compras in ListaP:
    print(compras)