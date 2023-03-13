tree = {"A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E", "F"],
        "D": ["B", "E", "G"],
        "E": ["C", "D", "G"],
        "F": ["C", "G"],
        "G": ["D", "E", "F"]
        }

cost = {
    "A-B": 10,
    "A-C": 28,
    "B-D": 25,
    "C-E": 14,
    "C-F": 16,
    "D-E": 24,
    "D-G": 22,
    "E-G": 18,
    "F-G": 12
}

"""
Can find minimum cost spanning tree by using Prims algorithm.
Spanning tree is a tree that not form cycle. 
Prims algorithm work like that: 
Set min cost edge firts.
Select next min selected to previos and form that continue the same logic till no node is repeted twice.
"""


def primsAlgorithm(tree: dict, cost: dict) -> set:
    spanningTree = {}
    currentNode = [x.split("-")[0]
                   for x, y in sorted(cost.items(), key=lambda v: v[1])][0]
    totalCost = 0
    while True:

        nextNodes = [x for x in tree[currentNode] if x not in spanningTree]
        if not nextNodes:
            break
        nextNode = nextNodes[0]
        costKey = f"{currentNode}-{nextNode}"
        if costKey not in cost:
            costKey = f"{nextNode}-{currentNode}"
        minCost = cost[costKey]

        for e in nextNodes[1:]:
            if (e not in spanningTree):
                costKey = f"{currentNode}-{e}"
                if (costKey not in cost):
                    costKey = f"{e}-{currentNode}"
                currCost = cost[costKey]
                if (currCost < minCost):
                    minCost = currCost
                    nextNode = e

        if (nextNode in spanningTree):
            break

        spanningTree[currentNode] = nextNode
        totalCost += minCost
        currentNode = nextNode

    return spanningTree, totalCost


if __name__ == '__main__':
    spanningTree, totalCost = primsAlgorithm(tree, cost)
    print(f"Tree -> {spanningTree}")
    print(f"Total Cost -> {totalCost}")
