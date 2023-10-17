def CuckTailSort(listUser):
    lenList = len(listUser)
    if lenList <= 1:
        return listUser
    sorted = False
    while not sorted:
        sorted = True
        for i in range(lenList-2, 0, -2):
            if listUser[i] > listUser[i+1]:
                listUser[i], listUser[i+1] = listUser[i+1], listUser[i]
                is_sorted = False
        for i in range(lenList-1, 2, -2):
            if listUser[i] < listUser[i-1]:
                listUser[i], listUser[i-1] = listUser[i-1], listUser[i]
                is_sorted = False
    return listUser

if __name__ == "__main__":
    print("holla")
    z = CuckTailSort([1,5,7,4,9])

    print(z)