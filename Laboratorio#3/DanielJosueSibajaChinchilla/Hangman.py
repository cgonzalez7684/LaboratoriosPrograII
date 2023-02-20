import random

class Hangman:
    
    def __init__(self):
        self.word_list = ["Caballo", "Abeja", "Naranja", "Azul", "Telefono", "Computadora"]
        self.selected_word = ""
        self.split_word = [] #Lista donde la palabra escogida se encuentra dividida por letra
        self.user_list = [] #Lista para almacenar el progreso del usuario durante el juego
    
    def remove(self, position):
        self.word_list.pop(position)
    
    def modify(self, position, word):
        self.remove(position)
        self.word_list.insert(position, word)
    
    def add(self, word):
        self.word_list.append(word)
        
    def word_picker(self):
        self.split_word = []
        self.selected_word = self.word_list[random.randrange(0, len(self.word_list))]
        for letter in self.selected_word:
            self.split_word.append(letter)
        
            
    def list_printer(self):
        print("\nCurrent list of words: \n")
        print("{0}     {1}".format("Position", "Words"))
        for i in range (len(self.word_list)):
            print("   {0}         {1}".format(i, self.word_list[i]))   
    
    def menu(self):
        print("---------------Hangman by DaNtR3---------------\n"
              "Bienvenido!\nEscoja una de las posibles opciones:\n"
              "1-Añadir palabras a la lista de juego\n"
              "2-Eliminar palabras de la lista de juego\n"
              "3-Modificar palabras de la lista de juego\n"
              "4-Imprimir lista de palabras existentes\n"
              "5-Empezar juego\n")
    
    def fill_user_list(self):
        for i in range(len(self.split_word)):
            self.user_list.append("_")
    
    def user_list_status(self):
        #for i in range(len(self.split_word)):
        print(" ".join(self.user_list))
    
    
    def checker (self, letter):
        for i in range (len(self.split_word)):
            if letter.lower() == self.split_word[i].lower():
                self.user_list.pop(i)
                self.user_list.insert(i, letter)
                