
tree = {
    1: (1,2),
    2: (3,4),
    3: (5,6),
    4: (7,8),
    5: (2,4),
    6: (2,5),
    7: (1,3),
    8: (6,8),
    9: (5,7)
}

# discArr = dict([(x,-1) for x in tree.keys()]) 

def elementInSet(set1:set, set2: set)-> bool:
    for el in set1:
        if el in set2: 
            return True
    return False


def findNrCycles(tree: dict) ->set: 
    # discDict = dict([(x,-1) for x in tree.keys()]) 
    discset =  set()
    cycleNr = 0     
    for key in tree.keys():
        elements =  tree[key]
        if not elementInSet(elements, discset): 
            discset.update(elements)
        else: 
            cycleNr +=1
    return discset, cycleNr 


if __name__ == '__main__':
    cycleNr, discArr = findNrCycles(tree)
    print(cycleNr)
    print(discArr)