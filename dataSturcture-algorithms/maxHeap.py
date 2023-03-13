import math


class MaxHeap:
    

    def __init__(self) -> None:
        self.__heap = []
        self.__removeList =[]
        self.__elements = 0

    def insert(self, element):
        self.__heap.append(element)
        self.__elements += 1
        self.__heapify(self.__elements-1)
        print(self.__heap)

    def delete(self):
        if(self.__elements==0 ):
            return None 
        elif(self.__elements==1):
            self.__elements = 0 
            return self.__heap.pop()

        else: 
            removed = self.__heap[0]
            self.__removeList.append(removed)
            self.__heap[0] = self.__heap.pop()
            self.__elements -=1
            self.__deleteHeapify(0)  
            return removed 

    def __heapify(self, index):
        if (index <= 0):
            return
        pIndex = math.floor(index/2)
        current = self.__heap[index]
        parent = self.__heap[pIndex]
        if (current > parent):
            self.__heap[pIndex] = current
            self.__heap[index] = parent

        self.__heapify(pIndex)
    
    def __deleteHeapify(self,index):
        leftInd =  index*2+1 
        rightInd =  index*2+2
        current =  self.__heap[index]
        if(rightInd>=self.__elements ):
            if(leftInd>=self.__elements):
                return
            else:
                swapInd = leftInd
        else:
            if(self.__heap[rightInd]>=self.__heap[leftInd]):
                swapInd = rightInd
            else:
                swapInd = leftInd

        if(current>=self.__heap[swapInd]):
            return
        else:
            self.__heap[index] = self.__heap[swapInd]
            self.__heap[swapInd] = current
            self.__deleteHeapify(swapInd)
        

    def getHeap(self) -> list:
        return self.__heap 

    def __setHeap(self, heap):
        self.__heap = heap
        self.__elements =  len(heap)

    def getRemovedList(self) -> list: 
        return self.__removeList

    def __str__(self) -> str:
        return self.__heap
    
    def heapSort(self) -> list:
        arr = []
        maxHeap =  MaxHeap()
        maxHeap.__setHeap(self.__heap.copy())
        
        while(True):
            el =  maxHeap.delete()
            if(el is None):
                break

            arr.append(el)

        return arr
    
    
if __name__ == "__main__":
    
    heap =  MaxHeap()
    heap.insert(50)
    heap.insert(70)
    heap.insert(33)
    heap.insert(53)
    heap.insert(12)   
    heap.insert(77)
    heap.insert(14)
    heap.insert(14)
    print(heap.getHeap())

    print(heap.heapSort())


    
    

