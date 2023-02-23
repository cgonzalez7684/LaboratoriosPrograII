petName=["Rosco","Burbuja","Jack"]
#This while help me to ask the user if want or not to continue...

continuar = True
while continuar:
    option = int(input("Main Menu.\n "+ " What would you like to do...? \n"+"\n1. Add a pet name. "+"\n2. Delete PetName. "+"\n3. Modify first petname. "+"\n4. Display list."+"\n5. Exit"))

    if (option==1):
     print("Enter a new pet name: ")
     petName.append(input())# Here you add a new petname into the list
    
     print("Pet name added..!!! "+ str(petName))
     print("The new list is: ")
     print(petName)# here displays an aupdate list
    elif(option==2):
      print("What  petname would u like to delete...?")
      print(petName)
      petName.remove(input())  #here u write the item that you want to remove from the list    
      print("The new list is: ")
      print(petName)
    elif(option==3):
       print("Please enter a new name instead of Rosco..!!")
       print(petName)#  here displays the updated list..
       petName[0] = input("Enter a new name: ")# here you modify the first item from the list only
       print("The new list is: ")
       print(petName)# here displays an aupdate list
    elif(option==4):
       print("The petnames are: ")
       
       for i in range(len(petName)):# This bring me the whole list of petnames..
         print("The petname -> "+ str(int(i) +1) +" is -> "+ petName[i])
         
    elif(option==5):
       print("Thanks, see you later..!!!")     
    else:
     print("Option, not found, please try again...!!")
 
# This cicle asks the user again if want or not to continue...    
    if(option!=5):    
         answer=input("Would you like to continue...? ")
         if answer == 'Y' or answer == 'y':
           pass
         else:
            continuar=False
    
 
 
