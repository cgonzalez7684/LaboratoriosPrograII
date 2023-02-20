"""
Universidad Internacional de las Américas UIA
Carrera: Ingeniería del Software
Curso: Programación II
Código propiedad de: Yadir Vega Espinoza
Evaluación: Laboratorio #3

Enunciado:
            Elabore un programa tipo consola que permita ejemplificar las acciones de agregar, 
            eliminar, modificar y recorrer una estructura tipo <list>, el contexto del desarrollo 
            queda a criterio del estudiante.
"""

# time para hacer delay en segundos al recorrer la lista y se vea mas lento
import time

# clase de operaciones
class operaciones:
    
    # constructor con la lista en donde operaremos, inicializada vacía 
    def __init__(self):
        self.lista_valores = []
    
    # permite iterar sobre una lista, dada la lista, además hace un delay en el print para ver el efecto recorrido
    def iterar_lista(self, lista):
        print("\nIterando sobre la lista " + str(self.lista_valores))
        for i in lista:
            print(i)
            time.sleep(0.8)

    # función que me permite pedir de manera estándar un valor
    def solicita_valor(self,op):
        entrada = input("\nIngrese el valor que desea " + op + ": ")
        return entrada

    # función que me permite agregar un valor a la lista, el valor es soclitado al usuario
    def agregar(self):
        entrada = self.solicita_valor("agregar")
        self.lista_valores.append(entrada)

    """función que me permite eliminar un valor de la lista, el valor a eliminar es solicitado al usuario
       si la lista es vacía no opera y notifica que esta vacía, si no está vacía pero el valor a eliminar no existe en la lista notifica que no existe
       si no está vacía y existe el valor a eliminar (condición de eliminado) se elimina.
    """
    def eliminar(self):
        if len(self.lista_valores) == 0:
            print("\n*******     Lista vacía")
        else:
            eliminar_val = self.solicita_valor("eliminar")
            if eliminar_val in self.lista_valores:
                self.lista_valores.remove(eliminar_val)
                print("\n*******     " + eliminar_val + " fue eliminado correctamente")
            else:
                print("\n*******     " + eliminar_val + " no existe en la lista, nada que eliminar")
    
    """función que me permite modificar un valor de la lista, el valor a modificar es solicitado al usuario
       si la lista es vacía no opera y notifica que esta vacía, si no está vacía pero el valor a modificar no existe en la lista notifica que no existe
       si no está vacía y existe el valor a modificar (condición de modificado) se solicita el nuevo valor y se modifica.
    """
    def modificar(self):
        if len(self.lista_valores) == 0:
            print("\n*******     Lista vacía")
        else:
            # valor actual
            modificar = self.solicita_valor("modificar")
            # guarda posiciones donde están los valores
            posiciones = []
            # saber las posiciones donde hay que modificar, puede ser una o varias
            if modificar in self.lista_valores:
                # valor nuevo
                modificado = self.solicita_valor("remplace a " + modificar)

                for i in range(len(self.lista_valores)):
                    if self.lista_valores[i] == modificar:
                        posiciones.append(i)
                        continue
                    else:
                        continue
            # si hay valores en la lista que coinciden con el que queremos modificar entonces modificamos
            if len(posiciones)>0:
                # para cada posicion modificamos en la lista general con el nuevo valor 
                for i in posiciones:
                    self.lista_valores[i] = modificado
                
                # notifica que fue modifcado correctamente
                print("\n*******     " + modificar + " fue modificado correctamente " + " por " + modificado)
            else:
                # notifica que no se eliminó
                print("\n*******     " + modificar + " no existe en la lista, nada que modificar")           

    # funcion que permite mostrar un menu de opciones
    def menu(self):
        while True:
            # pide al usuario un entero del 1 al 5 para agregar, eliminar, modificar, recorrer y salir del programa
            menu_op = int(input(("\nBienvenido, ingrese una opción\n\t" + 
                        "1) Agregar a lista\n\t2) Eliminar de la lista\n\t3) Modificar de la lista\n\t4) Recorrer la lista\n\t5) Salir\t>>")))
            # agrega en lista
            if menu_op==1:
                self.agregar()
            # elimina en lista
            if menu_op == 2:
                self.eliminar()
            # modifica en lista
            if menu_op ==3:
                self.modificar()
            # itera en lista
            if menu_op ==4:
                self.iterar_lista(self.lista_valores)
            # sale del programa
            if menu_op ==5:
                print("---------------- PROGRAMA TERMINADO CORRECTAMENTE ----------------\n\n")
                break
# Fin de la clase