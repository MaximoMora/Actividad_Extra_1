def CuckTailSort(listUser):
    # lenList = len(listUser)
    # change = True
    # start = 0
    # end = lenList - 1
    # while change == True:

    #     change = False
    #     for i in range(start, end):
    #         if (listUser[i] > listUser[i + 1]):
    #             listUser[i], listUser[i + 1] = listUser[i + 1], listUser[i]
    #             change = True

    #     if (change == False):
    #         break
    #     change = False
    #     end = end - 1
    #     for i in range(end - 1, start - 1, -1):
    #         if (listUser[i] > listUser[i + 1]):
    #             listUser[i], listUser[i + 1] = listUser[i + 1], listUser[i]
    #             change = True

    #     start = start + 1

    # return listUser
    for i in range(len(listUser), 0, -1):
        


if __name__ == "__main__":
    print("holla")
    lista = [1,5,7,4,9]
    z = CuckTailSort(lista)

    print(z)