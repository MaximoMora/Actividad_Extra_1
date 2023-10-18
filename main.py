import matplotlib.pyplot as plt
import numpy as np
import time
import random


class Algorithms():

    def __init__(self):
        self.listUser = []
        self.target = None

    def setTarget(self, userTarget):
        self.target = userTarget
        
    def setListUser(self, newlistUser):
        self.listUser = newlistUser
        

    def CuckTailSort(self):
        
        lenList = len(self.listUser)
        change = True
        start = 0
        end = lenList - 1
        history = [self.listUser.copy()]

        for i in range(len(self.listUser), 0, -1):
            for i in range(start, end):
                if (self.listUser[i] > self.listUser[i + 1]):
                    self.listUser[i], self.listUser[i + 1] = self.listUser[i + 1], self.listUser[i]
                    history.append(self.listUser.copy())

            if (change == False):
                break

            change = False
            end = end - 1

            for i in range(end - 1, start - 1, -1):
                if (self.listUser[i] > self.listUser[i + 1]):
                    self.listUser[i], self.listUser[i + 1] = self.listUser[i + 1], self.listUser[i]
                    history.append(self.listUser.copy())

        start = start + 1

        
        print(f"Lista ordenada: {self.listUser}")
        return history


def Welcome():
    print("""
          
>Ingresar lista 1
>Ingresar Numero a buscar 2
>buscar numero 3
          """)
if __name__ == "__main__":
    Welcome()
    
    userClass = Algorithms()
    userInput = int(input(">"))
    listUser = []
    if userInput == 1:
        exit = False
        print("Ingrese los numeros de la lista")
        while not exit:
            userNumber = input(">")
            if userNumber == "salir":
                exit = True
            elif type(userNumber) == "string":
                print("ingresa un numero")
            else:
                listUser.append(userNumber)
                
        userClass.setListUser(listUser)
        
    elif userInput == 2:
        print("Ingresa el numero a buscar")
        userNumber = int(input(">"))
        userClass.setTarget(userNumber)
        
    elif userInput == 3:
        userClass.CuckTailSort()
        
            
    
    
    
    
