
import random

class Hangman:
    
    def __init__(self):
        self.word_list = ["Caballo", "Abeja", "Naranja", "Azul", "Telefono", "Computadora"]
        self.selected_word = ""
        self.split_word = [] #Lista donde la palabra escogida se encuentra dividida por letra
        self.user_list = [] #Lista para almacenar el progreso del usuario durante el juego
        self.failures = 0
        self.stages = ["""  
                        
                                   
                                   
                                
                                      
                                
                        
                    _________
                        """, 
                        """  
                        
                        |           
                        |           
                        |           
                        |             
                        |          
                        |
                    ____|____
                        """,
                        
                        """  
                        -------------
                        |           
                        |           
                        |           
                        |              
                        |          
                        |
                    ____|____
                        """, 
                        
                        """  
                        -------------
                        |           |
                        |           |
                        |           
                        |               
                        |          
                        |
                    ____|____
                        """,
                        """  
                        -------------
                        |           |
                        |           |
                        |           O
                        |                 
                        |          
                        |
                    ____|____
                        """,
                        """  
                        -------------
                        |           |
                        |           |
                        |           O
                        |           |    
                        |           
                        |
                    ____|____
                        """,
                        """  
                        -------------
                        |           |
                        |           |
                        |           O
                        |         --|      
                        |           
                        |
                    ____|____
                        """, 
                        """  
                        -------------
                        |           |
                        |           |
                        |           O
                        |         --|--      
                        |           
                        |
                    ____|____
                        """,
                        """  
                        -------------
                        |           |
                        |           |
                        |           O
                        |         --|--      
                        |          / 
                        |
                    ____|____
                        """,
                           """  
                        -------------
                        |           |
                        |           |
                        |           O
                        |         --|--      
                        |          / \\
                        |
                    ____|____
                        """]
        
    
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
    
    
    def check_input (self, letter):
        for i in range (len(self.split_word)):
            if letter.lower() == self.split_word[i].lower():
                self.user_list.pop(i)
                self.user_list.insert(i, letter)
        if letter not in self.user_list:
            self.failures += 1
            print(self.failures)
 
    def game_status(self):
        print(self.stages[self.failures])
        print(" ".join(self.user_list))     
        
    
    
    def game_over(self):
        self.user_word = ""
        for i in self.user_list:
            self.user_word += i  
        if self.user_word.lower() == self.selected_word.lower():
            self.user_list.clear()
            self.failures = 0
            print("\n*******Felicidades! Ha encontrado la palabra*******\n",
                  "\nPalabra encontrada: ", self.selected_word)
            return True
        elif self.failures >= 9:
            self.user_list.clear()
            self.game_status()
            self.failures = 0
            print("\n*******No logro encontrar la palabra*******\n",
                  "\nPalabra a encontrar: ", self.selected_word)
            return True
        
            
        