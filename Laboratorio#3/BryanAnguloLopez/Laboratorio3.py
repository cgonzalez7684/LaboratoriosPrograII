Lista =["a","c","r","p","z","l","f","o","s"]
print("La lista inicial es: ")
print(Lista)

Lista.append("adios")
Lista.insert(5,"m")
print("Lista con datos agregados: ")
print(Lista)

Lista[2:5] = ["cambie", "Yo tambien","X3"]
print("Lista modificada: ")
print(Lista)

del Lista[4:6]
print("Lista sin los datos eliminados: ")
print(Lista)

print("Se recorre la lista en:")
for x in range(4,len(Lista)-2):
  print(Lista[x])

print("El tamaño de la lista es:")
print(len(Lista))

