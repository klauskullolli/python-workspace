graph = {"A": ["B", "C", "D"],
         "B": ["E", "F"],
         "C": ["E", "F"],
         "D": ["E", "F", "G"],
         "E": ["I"],
         "F": ["I"],
         "G": ["I"],
         "I": []}

dist = {
    ("A", "B"): 2,
    ("A", "C"): 1,
    ("A", "D"): 3,
    ("B", "E"): 2,
    ("B", "F"): 3,
    ("C", "E"): 6,
    ("C", "F"): 7,
    ("D", "E"): 6,
    ("D", "F"): 8,
    ("D", "G"): 9,
    ("E", "I"): 6,
    ("F", "I"): 4,
    ("G", "I"): 5
}

"""
Multi Stage graphs are graphs that work in leveles so element of a level can connect only
those to next level. So is used dynamic programming algorithm to solve the shortest distance path
form first to last level of the graph.
An examle graph can be like that: 
        B  
    _ /    \ _  
  /            \  
A ----  C ----  E
  \ _       _  /
      \   / 
        D
This is a 3 level graph  
- So for finding the shortest path firt of all if graph is in the form of map, 
convert each node into a 2D array so each node represent an index of represent the node. 
A cell in  2D array represent distance of nodes in this case (i,j) node distance is  arr[i][j] value
Next start from last node and use a dynamic formula fx node (A, B) distance is represented by i, j indexes
respectively and  cost(i) -> (min cost form ith node) so 
cost(i) =  min {distance(i,j) + cost(j), distance(i,k) + cost(k)}
distance(i,j) is the direct distance to j node that is an adjesent node of i. 
For every adjesent find the minimum one and save the dest of ith node the node that form the minimim cost. 
Save min cost in cost arr in the index of ith to access direcly form node.
Min destination in another array ex. dest array and in the ith index add short dest node.
"""


def formGraphArray(graph: dict, dist: dict):
    nodes = list(graph.keys())
    length = len(nodes)
    arrMap = []

    for i in range(0, length):
        node = nodes[i]
        row = []
        for j in range(0, length):
            nextNode = nodes[j]
            if (node, nextNode) in dist:
                row.append(dist[(node, nextNode)])
            else:
                row.append(0)
        arrMap.append(row)

    print(arrMap)

    return arrMap


def findShortestPath(graph: dict, dist: dict) -> list:
    nodes = list(graph.keys())
    arrMap = formGraphArray(graph, dist)
    length = len(nodes)
    lastIndex = length - 1
    cost = [None for _ in range(0, length)]
    dest = [None for _ in range(0, length)]
    cost[lastIndex] = 0

    for i in range(length - 2, -1, -1):
        min = 10000000000
        for j in range(i, length):
            if (arrMap[i][j] != 0 and arrMap[i][j] + cost[j] < min):
                min = arrMap[i][j] + cost[j]
                dest[i] = j
        cost[i] = min

    costDict = {k: v for k, v in zip(nodes, cost)}

    print(f"Costs for each node -> {costDict}")

    destDict = {}
    for k in range(length):
        if dest[k] != None:
            destDict[nodes[k]] = nodes[dest[k]]
        else:
            destDict[nodes[k]] = None

    print(f"Short destination for each node -> {destDict}")

    path = []
    path.append(nodes[0])
    i = dest[0]
    while True:
        if i is None:
            break
        path.append(nodes[i])
        i = dest[i]

    print(f"Shortest path -> {path}")
    return path, cost[0]


if __name__ == '__main__':
    shortestPath, minCost = findShortestPath(graph,  dist)
