import sys
import time
sys.setrecursionlimit(2000)

n=5
arr1 = [x for x in range(1, n+1)]
arr2 = []
arr3 = []

field = [arr1, arr2, arr3]

length = len(field)

primarArrLen = len(arr1)


def calculate(field):
    if (primarArrLen % 2 == 0):
        moveElementEven(field, 0, None)
    else:
        moveElementOdd(field, 0, None)


def moveElementEven(field, currentIndex, prev):
    print(field)
    print("--------------------------------------------------------")
    currentIndex = currentIndex % length
    if (len(field[length-1]) == primarArrLen or len(field[length-2]) == primarArrLen):
        return

    if (field[currentIndex]):
        el = field[currentIndex][0]

        if (prev is None or el != prev):
            iter = 1
            insert_index = None

            while (iter < length):
                ceckIndex = (currentIndex + iter) % length

                if (not field[ceckIndex] or field[ceckIndex][0] > el):
                    insert_index = ceckIndex
                    break
                iter += 1

            if (insert_index is not None):
                el = field[currentIndex].pop(0)
                field[ceckIndex].insert(0, el)
                moveElementEven(field, currentIndex, el)
            else:
                moveElementEven(field, currentIndex+1, prev)
        else:
            moveElementEven(field, currentIndex+1, prev)
    else:
        moveElementEven(field, currentIndex+1, prev)


def moveElementOdd(field, currentIndex, prev):
    print(field)
    print("--------------------------------------------------------")
    currentIndex = currentIndex % -length
    if (len(field[length-1]) == primarArrLen or len(field[length-2]) == primarArrLen):
        return

    if (field[currentIndex]):
        el = field[currentIndex][0]

        if (prev is None or el != prev):
            iter = 1
            insert_index = None

            while (iter < length):
                ceckIndex = (currentIndex - iter) % -length

                if (not field[ceckIndex] or field[ceckIndex][0] > el):
                    insert_index = ceckIndex
                    break
                iter += 1

            if (insert_index is not None):
                el = field[currentIndex].pop(0)
                field[ceckIndex].insert(0, el)
                moveElementOdd(field, currentIndex, el)
            else:
                moveElementOdd(field, currentIndex-1, prev)
        else:
            moveElementOdd(field, currentIndex-1, prev)
    else:
        moveElementOdd(field, currentIndex-1, prev)


if __name__ == "__main__":

    start = time.time()
    calculate(field)
    end = time.time()
    print(f"\nTotal procesing time {end-start}s")
