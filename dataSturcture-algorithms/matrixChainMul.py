
matrixDimMap = {
    "A1": [3, 2],
    "A2": [2, 4],
    "A3": [4, 2],
    "A4": [2, 5]
}


def createDimensionArr(matrixDimMap: dict) -> list:
    arr = []
    i = 0 
    for el in matrixDimMap.values():
        if  i == 0 : 
            [arr.append(x) for x  in el]
        else: 
            [arr.append(x) for x in el[1::]]
        i +=1
    return arr


def generateCostAndDividePositionMatrix(matrixDimMap: dict):
    dictionary = {
        "C-matrix": None,
        "K-matrix": None
    }
    dimensionArr = createDimensionArr(matrixDimMap)
    length = len(matrixDimMap.keys())
    cMatrix = []
    for i in range(length):
        arr = []
        for j in range(length):
            if j == i:
                arr.append(0)
            else:
                arr.append(None)
        cMatrix.append(arr)

    kMatrix = [[None for _ in range(length)] for _ in range(length)]

    step = 1

    while step < length:
        i = 0
        j = step
        while j < length:
            if i == j:
                i += 1
                j += 1
            else:
                min = cMatrix[i][j]
                for k in range(i, j):
                    cost = cMatrix[i][k] + cMatrix[k+1][j] + dimensionArr[i]*dimensionArr[k]*dimensionArr[j+1]
                    if min is None or cost < min:
                        min = cost
                        kMatrix[i][j] = k
                cMatrix[i][j] = min
                i += 1
                j += 1
        step += 1
        
    dictionary["C-matrix"] = cMatrix
    dictionary["K-matrix"] = kMatrix
        
    return dictionary

def multiplyOrder(matrixDimMap: dict):
    keyArr = []
    length  = 0  
    for el in matrixDimMap.keys():
        keyArr.append(el)
        length +=1 
        
    dividePosMatrix =  generateCostAndDividePositionMatrix(matrixDimMap)["K-matrix"]
    i = 0 
    j =  length-1
    levelOrder =  []
    while abs(j - i) >=2 : 
        k =  dividePosMatrix[i][j]
        
        j = k 
    
        
         
    
    
    
    
    pass

if __name__ == '__main__':

    a = [1,3]
    print(a[0:0])    

    print(generateCostAndDividePositionMatrix(matrixDimMap))
