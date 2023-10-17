import matplotlib.pyplot as plt
import numpy as np
import time, random

def CuckTailSort(listUser):
    lenList = len(listUser)
    change = True
    start = 0
    end = lenList - 1
    history = [listUser.copy()]

    for i in range(len(listUser), 0, -1):
        for i in range(start, end):
            if (listUser[i] > listUser[i + 1]):
                listUser[i], listUser[i + 1] = listUser[i + 1], listUser[i]
                history.append(listUser.copy())

    #     if (change == False):
    #         break
    #     change = False
    #     end = end - 1
    #     for i in range(end - 1, start - 1, -1):
    #         if (listUser[i] > listUser[i + 1]):
    #             listUser[i], listUser[i + 1] = listUser[i + 1], listUser[i]
    #             change = True
        if (change == False):
            break

        change = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if (listUser[i] > listUser[i + 1]):
                listUser[i], listUser[i + 1] = listUser[i + 1], listUser[i]
                history.append(listUser.copy())

    #     start = start + 1

    # return listUser
    for i in range(len(listUser), 0, -1):
        


if __name__ == "__main__":
    lista = [random.randint(1, 100) for _ in range(100)]
    print("Original list:", lista)
    history = CuckTailSort(lista)

    fig, ax = plt.subplots()

    for i, step in enumerate(history):
        colors = ['red' if j == len(step) - 2 or j == len(step) - 1 else 'lime' for j in range(len(step))]
        ax.bar(np.arange(len(step)), step, color=colors)
        ax.set_title(f'Step {i + 1}')
        plt.pause(0.05)
        ax.clear()

    plt.show()
