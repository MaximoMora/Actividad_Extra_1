import math


def jumpSearch(listUser,target):
    
    n = len(listUser)
    nMath = int(math.sqrt(n))
    nSum = nMath
    min = 0
    max = nMath
        
    while listUser[nMath] < target:
        min = nMath
        max += nSum
        
        nMath += nSum
        
    print(min)
    print(max)
    print("index",nMath)
    print("numero a buscar",target)
    
    for i in range(min,max+1):
        if listUser[i] == target:
            
            print("encontrado")
            print(f"el numero {target} esta en la posicion {i}")


    
    
jumpSearch([1,2,3,4,5],4)