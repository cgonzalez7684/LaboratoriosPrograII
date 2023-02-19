"""
Universidad Internacional de las Américas UIA
Carrera: Ingeniería del Software
Curso: Programación II
Código propiedad de: Yadir Vega Espinoza
Evaluación: Laboratorio #3

Descripción: 
            Clase principal llamada main que invoca a las operaciones solicitadas en el enunciado del lab#2 desde operaciones_list.py

"""

# importo las operaciones creadas en el otro archivo
from operaciones_list import *

# clase principal
class main:
    if __name__ == "__main__":
        # Instancia de la clase operaciones
        app= operaciones()
        # Llamo al menu por medio de la instancia
        app.menu()