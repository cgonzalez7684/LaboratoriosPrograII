""""
alumnos= ['Ana', 'Carlos', 'Mario', 'María']
print(alumnos)
"""

#crear una lista de alumnos
alumnos=[]
n=int(input("¿Cuantos alumnos nuevos se van a ingresar?"))
for i in range(n):
    nombre=input("Ingrese el Nombre")
    alumnos.append(nombre)

print(alumnos)
