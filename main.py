


def bubble_sort(listUser):

    for i in range(len(listUser)):

        for j in range(len(listUser)-1-i):
            if listUser[j+1] < listUser[j]:
                listUser[j+1],listUser[j] = listUser[j],listUser[j+1]


    return listUser


if __name__ == "__main__":
    print("holla")
    z = bubble_sort([1,5,7,4,9])

    print(z)