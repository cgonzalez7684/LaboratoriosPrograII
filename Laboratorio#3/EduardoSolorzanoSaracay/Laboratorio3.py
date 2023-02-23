Materias = []
menu = int(0)
while (menu != 5):
    print ("---------------------------------")
    print ("Materias matriculadas en IQ 2023")
    print ("1) Ingresar materias")
    print ("2) Modificar materias")
    print ("3) Eliminar materias")
    print ("4) Materias matriculadas")
    print ("5) Cerrar aplicacion")
    print ("---------------------------------")
    menu = int(input ())
    if (menu == 1):
        print ("Ingrese el nombre de la materia que matriculo")
        Materias.append(input())
    elif (menu == 2):
        print("Ingrese el nombre de la materia que desea modificar")
        print(Materias)
        Materias.remove(input())
        print("Ingrese el nuevo nombre de la materia")
        Materias.append(input())
        print("Materia editada exitosamente")
    elif (menu == 3):
        print("Ingrese el nombre de la materia que desea eliminar")
        print(Materias)
        Materias.remove(input())
    elif (menu == 4):
        print(Materias)