
lista1 = ["Flauta","Guitarra","Oboe","Violin","Cello","Viola","Piccolo","Piano","Bateria"]
print (lista1)

for x in lista1:
    print(x)


lista1.append(input("Escriba el nuevo instrumento"))

for xx in lista1:
    print (xx)



for x in lista1:
    if x == "Viola":
        lista1.remove("Viola")


for xx in lista1:
    print (xx)
