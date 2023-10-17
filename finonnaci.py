def get_min_index(arr):
    fib2 = 0
    fib1 = 1
    fibm = fib2 + fib1

    while (fibm < len(arr)):
        fib2 = fib1
        fib1 = fibm
        fibm = fib2 + fib1
        
    return min(fibm,len(arr) - 1)






def fibonacci_search(arr, x):
    n = len(arr)
    min_index = get_min_index(arr)

    print("min: ",min_index)
    print("len: ",n)
    
    
    while (min_index < n):
        if (arr[min_index] < x):
            min_index += 1
        elif (arr[min_index] > x):
            min_index -= 1
            print("baja en uno el index",min_index)
        else:
            return min_index

    return -1

# Prueba
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
x = 85


minmo = get_min_index(arr)
print(minmo)


print(f"El elemento {x} está en el índice {fibonacci_search(arr, x)}")