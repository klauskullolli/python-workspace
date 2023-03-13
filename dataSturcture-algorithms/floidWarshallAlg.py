graph = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["A", "D"],
    "D": ["A"]
}


dist = {
    ("A", "B"): 2,
    ("A", "D"): 7,
    ("B", "A"): 8,
    ("B", "C"): 2,
    ("C", "A"): 5,
    ("C", "D"): 1,
    ("D", "A"): 2
}
"""
Floid Warshall Algorithm is the Dijkstra algorithm to find the shortest path to each node with each node.
Dijkstra is just to calculate shortest distance from 1 node. 
"""


def convertToAdjesentArr(graph: dict, dist: dict) -> list:
    nodes = list(graph.keys())
    length = len(nodes)

    arrAdj = []
    for i in range(0, length):
        arr = []
        for j in range(0, length):
            if (i == j):
                arr.append(0)
            elif ((nodes[i], nodes[j]) in dist):
                arr.append(dist[(nodes[i], nodes[j])])
            else:
                arr.append(None)
        arrAdj.append(arr)

    return arrAdj


def findMin(directDist, firstInd, secondInd):
    indirectVal = None
    if (firstInd != None and secondInd != None):
        indirectVal = firstInd + secondInd

    if (directDist == None and indirectVal == None):
        return None
    elif (directDist != None and indirectVal != None):
        return min(directDist, indirectVal)
    else:
        if (directDist == None):
            return indirectVal
        else:
            return directDist


def shortestDistArr(graph: dict, dist: dict) -> list:
    nodes = list(graph.keys())
    length = len(nodes)
    shortPathMatrix = convertToAdjesentArr(graph, dist)

    for k in range(length):
        for i in range(length):
            for j in range(length):
                if (i == k or j == k):
                    continue
                shortPathMatrix[i][j] = findMin(
                    shortPathMatrix[i][j], shortPathMatrix[i][k], shortPathMatrix[k][j])
    print(f"Shortest Path Matrix -> {shortPathMatrix}")

    return shortPathMatrix


if __name__ == "__main__":

    shortPathMatrix = shortestDistArr(graph, dist)
    nodes = list(graph.keys())
    shortDistMap = {}
    for i in range(len(shortPathMatrix)):
        for j in range(len(shortPathMatrix[0])):
            if (shortPathMatrix[i][j] is None):
                continue
            shortDistMap[(nodes[i], nodes[j])] = shortPathMatrix[i][j]

    print(f"Shortest distance between nodes -> {shortDistMap}")
