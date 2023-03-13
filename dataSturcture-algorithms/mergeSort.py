
# asceding
def mergeSort(arr: list, asc: bool):
    arrLen = len(arr)
    if (arrLen > 1):
        mid = arrLen // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L, asc)
        mergeSort(R, asc)
        mergeSort2List(arr, L, R, asc)

# reallocating existing positions of the array (faster)
def mergeSort2List(arr: list, a: list, b: list, asc: bool):
    m = len(a)
    n = len(b)
    i, j, k = 0, 0, 0

    while (i < m and j < n):
        if(asc):
            if (a[i] > b[j]):
                arr[k] = b[j]
                j += 1
            else:
                arr[k] = a[i]
                i += 1
        
        else:
            if (a[i] < b[j]):
                arr[k] = b[j]
                j += 1
            else:
                arr[k] = a[i]
                i += 1
        k += 1

    for _i in range(i, m):
        arr[k] = a[_i]
        k += 1
    for _j in range(j, n):
        arr[k] = b[_j]
        k += 1

#using clear method to empty the array every time performing the function 
def mergeSort2List1(arr: list, a: list, b: list) -> list:
    m = len(a)
    n = len(b)
    i, j = 0, 0
    arr.clear()

    while (i < m and j < n):
        if (a[i] > b[j]):
            arr.append(b[j])
            j += 1
        else:
            arr.append(a[i])
            i += 1

    for _i in range(i, m):
        arr.append(a[_i])

    for _j in range(j, n):
        arr.append(b[_j])


if __name__ == "__main__":
    arr = [1, 4, 2, 11, 5, 9, 6, 2, 25, 16]
    mergeSort(arr ,True)
    print(arr)
