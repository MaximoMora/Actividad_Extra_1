import matplotlib.pyplot as plt
import numpy as np
import time
import random
import math


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



    def JumpSearch(self):
        
    
        n = len(self.listUser)
        nMath = int(math.sqrt(n))
        nSum = nMath
        min = 0
        max = nMath
        
        while int(self.listUser[nMath]) < self.target:
            min = nMath
            max += nSum
        
            nMath += nSum
        
        print(min)
        print(max)
        print("index",nMath)
        print("numero a buscar",self.target)
    
        for i in range(min,max+1):
            if int(self.listUser[i]) == self.target:
            
                print("encontrado")
                print(f"el numero {self.target} esta en la posicion {i}")
    
def Welcome():
    print("""
          
>Ingresar lista 1
>Ingresar Numero a buscar 2
>ordenar lista
>buscar numero
          """)
if __name__ == "__main__":
    print(type("dasdada"))
    userClass = Algorithms()
    listUser = []
    exit = False

    while not exit:
        Welcome()

        userInput = input(">")

        if userInput == "salir":
            exit = True
        elif userInput == "1":
            NumberExit = False

            print("Ingrese los numeros de la lista, para salir 'exit'")
            while not NumberExit:
                userNumber = input("numeros >")
                if userNumber == "exit":
                    NumberExit = False
                    break

                elif type(userNumber) == "str":
                    print("ingresa un numero")
                else:
                    listUser.append(userNumber)
                
            userClass.setListUser(listUser)
            
            print("salio de escribir mas numeros en la lista")
        
        elif userInput == "2":
            print("Ingresa el numero a buscar")
            userNumber = int(input(">"))
            userClass.setTarget(userNumber)
        
        elif userInput == "3":
            userClass.CuckTailSort()
            
        elif userInput == "4":
            userClass.JumpSearch()
        
            
    
    
    
    
