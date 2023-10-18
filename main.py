import time, random, math
from colorama import Fore, Style

class Algorithms():

    def __init__(self):
        self.listUser = []
        self.target = None

    def setTarget(self, userTarget):
        self.target = userTarget

    def setListUser(self, newlistUser):
        self.listUser = newlistUser


    def CockTailSort(self):
        lenList = len(self.listUser)
        history = [self.listUser.copy()]

        def print_colored_list(lst, highlighted_index):
            for i, num in enumerate(lst):
                if i == highlighted_index:
                    print(Fore.RED + str(num) + Style.RESET_ALL, end=" ")
                else:
                    print(str(num), end=" ")
            print()

        for _ in range(len(self.listUser) - 1):
            change = False
            start = 0
            end = lenList - 1

            for i in range(start, end):
                if self.listUser[i] > self.listUser[i + 1]:
                    self.listUser[i], self.listUser[i + 1] = self.listUser[i + 1], self.listUser[i]
                    history.append(self.listUser.copy())
                    print_colored_list(self.listUser, i + 1)
                    time.sleep(0.025)
                    change = True

            if not change:
                break

            end = end - 1

            for i in range(end - 1, start - 1, -1):
                if self.listUser[i] > self.listUser[i + 1]:
                    self.listUser[i], self.listUser[i + 1] = self.listUser[i + 1], self.listUser[i]
                    history.append(self.listUser.copy())
                    print_colored_list(self.listUser, i)
                    time.sleep(0.025)

            start = start + 1

        print(f"Lista ordenada:\n {self.listUser}")
        return history

    def JumpSearch(self):
        n = len(self.listUser)
        nMath = int(math.sqrt(n))
        nSum = nMath
        min_idx = 0
        max_idx = nMath

        def print_colored_list(lst, target_idx, current_idx):
            for i, num in enumerate(lst):
                if i == target_idx:
                    print(Fore.GREEN + str(num) + Style.RESET_ALL, end=" ")
                elif i == current_idx:
                    print(Fore.RED + str(num) + Style.RESET_ALL, end=" ")
                else:
                    print(str(num), end=" ")
            print()

        found = False
        while nMath < n:
            if int(self.listUser[nMath]) >= self.target:
                print_colored_list(self.listUser, -1, nMath)
                break
            min_idx = nMath
            max_idx += nSum
            nMath += nSum
            print(f"Salto: min_idx={min_idx}, max_idx={max_idx}, nMath={nMath}")
            print_colored_list(self.listUser, -1, nMath)
            time.sleep(0.2)

        for i in range(min_idx, min(max_idx + 1, n)):
            if int(self.listUser[i]) == self.target:
                found = True
                print_colored_list(self.listUser, i, -1)
                print(f"Comparando con el número en la posición {i}")
                print(f"El número {self.target} está en la posición {i}")
                break
            else:
                print(f"Comparando con el número en la posición {i}")

        if not found:
            print("El número no se encontró en la lista.")




def Welcome():
    print("""
1. Ingresar Lista
2. Ordenar lista
3. Buscar!

4. Ver Lista
5. Usar lista predefinida

""")


if __name__ == "__main__":

    userClass = Algorithms()
    listUser = []
    exit = False

    while not exit:
        Welcome()

        userInput = input("> ")

        if userInput == "salir":
            exit = True
        elif userInput == "1":
            Exit = False

            print("Ingrese los numeros de la lista, para salir 'exit'")

            while not Exit:
                userNumber = input("> ")
                try:
                    try:
                        listUser.append(int(userNumber))
                    except:
                        listUser.append(float(userNumber))
                except:
                    if userNumber == "exit" or userNumber == "Exit":
                        Exit = False
                        break

            userClass.setListUser(listUser)

            print(f"Lista actual de numeros: {listUser}")

        elif userInput == "2":
            userClass.CockTailSort()

        elif userInput == "3":
            print("Ingresa el numero a buscar")
            userNumber = int(input(">"))
            userClass.setTarget(userNumber)
            userClass.JumpSearch()

        elif userInput == "4":
            print(listUser)

        elif userInput == "5":
            Exit = False
            while not Exit:
                try:
                    list_length = int(
                        input("Ingrese el largo de la lista: "))
                    listUser = [random.randint(1, 100) for _ in range(list_length)]
                    userClass.setListUser(listUser)
                    print(userClass.listUser)
                    Exit = True
                except:
                    print("Ingrese un numero válido")
                    break