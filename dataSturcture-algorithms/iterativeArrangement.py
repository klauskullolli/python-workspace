import time

n = 15

arr1 = [x for x in range(1, n+1)]
arr2 = []
arr3 = []

field = [arr1, arr2, arr3]

length = len(field)

primarArrLen = len(arr1)


def calculate(field):
    odd = primarArrLen % 2
    moveElement(field, 0, None, odd)
   


def moveElement(field, currentIndex, prev, odd):

    while True:
        print(field)
        print("--------------------------------------------------------")

        if odd == 1:
            currentIndex = currentIndex % -length
        else:
            currentIndex = currentIndex % length
        if (len(field[length-1]) == primarArrLen or len(field[length-2]) == primarArrLen):
            break

        if (field[currentIndex]):
            el = field[currentIndex][0]

            if (prev is None or el != prev):
                iter = 1
                insert_index = None

                while (iter < length):
                    if odd == 1:
                        ceckIndex = (currentIndex - iter) % -length
                    else:
                        ceckIndex = (currentIndex + iter) % length

                    if (not field[ceckIndex] or field[ceckIndex][0] > el):
                        insert_index = ceckIndex
                        break
                    iter += 1

                if (insert_index is not None):
                    el = field[currentIndex].pop(0)
                    field[insert_index].insert(0, el)
                    prev = el
                else:
                    if odd ==1:
                        currentIndex -= 1
                    else:
                        currentIndex += 1
            else:
                if odd ==1:
                    currentIndex -= 1
                else:
                    currentIndex += 1
        else:
            if odd ==1:
                    currentIndex -= 1
            else:
                currentIndex += 1
            


if __name__ == "__main__":

    start = time.time()
    calculate(field)
    end = time.time()
    print(f"\nTotal procesing time {end-start}s")
