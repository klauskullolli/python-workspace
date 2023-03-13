import copy
import math


# point class
class Point:
    
    
    def __init__(self,name, x, y) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.distance = 0

            
# calcuate distance between points
def distance(p1: Point, p2: Point): 
    return math.sqrt(abs(p1.x - p2.x)**2 + abs(p1.x - p2.x)**2) 

# remove point accoring name
def remove(p1 , points):
    for p in points:
        if p.name == p1.name:
            del p 
            break

# remove point accoring name
def minDistance(points: list[Point]):
    return min(points , key= lambda p : p.distance)

# this is the function that calculate the shortest path     
def TSP(points: list[Point]):
    
    path = [points[0].name]
    p = points.pop(0)
    dist = 0
    while True:
        if len(points)==0:
            break 
        copyPoints = copy.deepcopy(points)
        for el in copyPoints :
            el.distance = (p ,el)
        
        min = minDistance(copyPoints)
        dist +=min.distance 
        p = min
        path.append(min.name) 
        remove(p , points)
    
    return path , dist 

def loadFromFile():
    points = []
    with open("input.txt", "r") as file:
        file.readline()
        lines = file.readlines()
        for line in lines:
            arr = line.split(" ")
            points.append(Point(arr[0], float(arr[1], float(arr[2]))))
        file.close()
    return points     


if __name__ == "__main__":
    points = loadFromFile()
    path , dist  = TSP(points)
    
    print(path)
    
    for el in path :
        print(el)