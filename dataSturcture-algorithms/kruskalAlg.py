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


def findSpanningJoins(cost: dict):
    costCopy = [k.split("-")
                     for k, _ in sorted(cost.items(), key=lambda x: x[1])]  
    spanningJoins = {}
    revNodesList = [] 
    while costCopy:
        print (f"Spanning Joins -> {spanningJoins}")
        smallNode = costCopy[0]
        k, v = smallNode
        if (k in revNodesList  and v in revNodesList):
            del costCopy[0]    
            continue
        else:
            if(k in spanningJoins  and v in spanningJoins):
                del costCopy[0]    
                continue
            else:
                if k not in spanningJoins:
                    spanningJoins[k] =  v
                else:
                    spanningJoins[v] = k 
                del costCopy[f"{k}-{v}"]                
        


def kruskalsAlgorithms(tree: dict, cost: dict):
    costCopy = {k: v for k, v in cost.items()}
    spanningTree = {}
    revSpanningTree = {}
    totalCost = 0

    pass


if __name__ == "__main__":
    findSpanningJoins(cost)