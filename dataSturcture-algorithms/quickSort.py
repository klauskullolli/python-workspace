"""
Best case for quick sort is O(nlogn)
Worst case is when list is already sorted O(n^2)
Worst case can be escaped using as pivot:
- The middle element always
- Selecting the pivot random
    
"""
def quickSort(arr: list , asc:bool):
    doQuickSort(arr , 0 , len(arr), asc)


def doQuickSort(arr:list, l:int, h:int, asc: bool):
    if(l<h):
        j = newPivot(arr, l, h, asc)
        doQuickSort(arr, l, j, asc)
        doQuickSort(arr, j + 1, h, asc)
        


def newPivot(arr:list, l:int, h:int, asc: bool):
    pivot = arr[l]
    i = l + 1
    j = h-1
    while (i <= j):
        if asc :
            if (arr[i] > pivot):
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
                continue
        else:
              if (arr[i]<pivot):
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
                continue
        i += 1
    arr[l], arr[j] = arr[j], arr[l]

    return j


if __name__ == '__main__':
    arr = [3, 19, 21, 22, 23, 31, 32, 45]
    quickSort(arr, asc=False)
    print(arr)
