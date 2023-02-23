listaEstudiantes = []

def encabezadoSistema():
    print("----------------------------------")   
    print("1: Agregar estudiante a la clase")
    print("2: Eliminar estudiante de la clase")
    print("3: Modificar un estudiante de la clase")
    print("4: Mostrar lista de estudiantes de la clase")
    print("5: Salir")
    print("----------------------------------")
    
def agregarEstudiante():
    listaEstudiantes.append(str(input("Digite el nombre del estudiante que desea agregar: ")))
    
def eliminarEstudiante():
    estudiante = str(input("Digite el nombre del estudiante que desea eliminar de la clase: "))
    if estudiante in listaEstudiantes:
        listaEstudiantes.remove(estudiante)
        print(f"El estudiante {estudiante} ha sido eliminado")
    else:
        print(f"El estudiante {estudiante} no existe")
        
def modificarEstudiante():
    estudiante = str(input("Digite el nombre del estudiante que desea modificar en la clase: "))
    if estudiante in listaEstudiantes:
        index = listaEstudiantes.index(estudiante)
        listaEstudiantes[index] = str(input("Digite el nombre del nuevo estudiante: "))
    else: 
        print(f"El estudiante {estudiante} no existe")
    
    
def mostrarEstudiantes():
    print("Los Nombres de la lista son:")
    for Estudiante in listaEstudiantes:
        print(Estudiante)
    
def main():  
    while True:
        encabezadoSistema()
        opcion = int(input("Digite la opción sistema: "))
        if (opcion == 1):
            agregarEstudiante()
        elif (opcion == 2):  
            eliminarEstudiante()    
        elif (opcion == 3):  
            modificarEstudiante()       
        elif (opcion == 4):  
            print("Muchas gracias")
            mostrarEstudiantes()           
        elif (opcion == 5):  
            break     
        else: #y sino
            print("Opcion invalida, debe de ser del 1 - 5")
            continue
        
if __name__ == "__main__":
    main()