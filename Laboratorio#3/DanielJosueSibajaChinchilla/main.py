from Hangman import Hangman

class Game:
    
    def __init__(self):
        self.hangman = Hangman() #Inicializacion de la clase 
        self.game_on = True
        self.option = 0
        
    def game_loop(self):
        while True:
            self.hangman.menu()
            self.option = int(input())
            if (self.option == 1):
                self.hangman.add(str(input("\nIngrese la palabra que desee agregar a la lista: ")))
                
            elif (self.option == 2):
                self.hangman.list_printer()
                self.hangman.remove(int(input("\nIngrese el numero de posicion de la palabra que desea eliminar: ")))
                
            elif (self.option == 3):
                self.hangman.list_printer()
                self.pos = int(input("\nIngrese el numero de posicion de la palabra que desea modificar: "))
                self.word = str(input("\nIngrese la modificacion: "))
                self.hangman.modify(self.pos, self.word)
                
            elif (self.option == 4):
                self.hangman.list_printer()
                
            elif (self.option == 5):
                self.hangman.word_picker()
                self.hangman.fill_user_list()
                while (self.game_on):
                    self.hangman.user_list_status()
                    self.hangman.checker(str(input("\nIngrese una letra: ")))
            else:
                print("La opción ingresada no es válida")
      
        

if __name__ == "__main__":
    Game().game_loop()
    