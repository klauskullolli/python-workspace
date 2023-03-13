
# create a hexagon class that contain coordinates previous hexagon
# that brings to this state and distance as long as we are using A star algorithm
class Hexagon:

    def __init__(self, x, y, previous):
        self.x = x
        self.y = y
        self.previous = previous
        if self.previous is None:
            self.distance = 0
        else:
            self.distance = self.previous.distance + hexagonGridDistance(previous, self)

    # is needed to covert the hexagon to a dictionary
    def toDict(self)->dict:
        return {
            "x": self.x,
            "y": self.y,
            "distance": self.distance,
            "previous": {"x": self.previous.x,
                         "y": self.previous.y,
                         "distance": self.previous.distance} if self.previous is not None else None
        }

# function used to load data form file to a dictionary
def uploadInputData(fileName):
    with open(fileName) as f:
        dict = {}
        dict["dimensions"] = [int(x) for x in f.readline().split(" ")]
        dict["starting"] = [int(x) for x in f.readline().split(" ")]
        dict["ending"] = [int(x) for x in f.readline().split(" ")]
        dict["blocking_number"] = int(f.readline())
        blocking_cordinates = []

        for line in f:
            blocking_cordinates.append([int(x) for x in line.split(" ")])
        dict["blocked_cordinates"] = blocking_cordinates

        return dict

# this is the heteros function used to calculate the distance
def hexagonGridDistance(h1: Hexagon, h2: Hexagon) -> int:
    dx = h1.x - h2.x
    dy = (int(h1.x / 2) + h1.y) - (int(h2.x / 2) + h2.y)
    if (dx > 0 and dy < 0) or (dx < 0 and dy > 0):
        return abs(dx) + abs(dy)
    else:
        return max(abs(dx), abs(dy))

# this function used to check if a hexagon is inside specified boundaries and not part of blocked list
def isAllowedMove(h1: Hexagon, max_x, max_y, blockedList):

    if (h1.x >= 0 and h1.x < max_x) and (h1.y >= 0 and h1.y < max_y) and ([h1.x, h1.y] not in blockedList):
        return True

    else:
        return False

# this function generate all possible move form a hexagon to other
def expandHexagonal(h1: Hexagon, max_x, max_y, blockedList):

    # different movement direction if row is even and different moves is odd
    if(h1.x%2==0):
        moves = [move for move in [Hexagon(h1.x-1, h1.y, previous=h1),
                                   Hexagon(h1.x - 1, h1.y + 1, previous=h1),
                                   Hexagon(h1.x, h1.y + 1, previous=h1),
                                   Hexagon(h1.x + 1, h1.y + 1, previous=h1),
                                   Hexagon(h1.x+1, h1.y, previous=h1),
                                   Hexagon(h1.x, h1.y - 1, previous=h1)] if isAllowedMove(move, max_x, max_y, blockedList)]
        return moves
    else:
        moves = [move for move in [Hexagon(h1.x-1, h1.y - 1, previous=h1),
                                   Hexagon(h1.x - 1, h1.y, previous=h1),
                                   Hexagon(h1.x, h1.y + 1, previous=h1),
                                   Hexagon(h1.x + 1, h1.y, previous=h1),
                                   Hexagon(h1.x + 1, h1.y - 1, previous=h1),
                                   Hexagon(h1.x, h1.y - 1, previous=h1)] if
                 isAllowedMove(move, max_x, max_y, blockedList)]
        return moves

# implementation off A Star algorithm
def AStar(start: Hexagon, max_x, max_y, end_x, end_y, blockedList):
    queue = [start]
    while queue:
        # lowest cost will be expanded fist
        h = queue.pop(0)
        blockedList.append([h.x, h.y])
        print(h.toDict())
        if end_x == h.x and end_y == h.y:
            return h

        # add to the queue possible moves
        queue = queue + expandHexagonal(h, max_x, max_y, blockedList)

        # queue data are sorted according to the lowest cost
        queue = sorted(queue, key=lambda hex: hex.distance)
    return False

if __name__ == "__main__":
    dictionary = uploadInputData("input.txt")
    for key, value in dictionary.items():
        print(f"{key} : {value}")

    max_x, max_y = dictionary["dimensions"]
    start_x , start_y = dictionary["starting"]
    start = Hexagon(start_x, start_y, None)
    end_x, end_y = dictionary["ending"]
    blckLs = dictionary["blocked_cordinates"]
    moves = expandHexagonal(start, max_x, max_y, blckLs)

    result = AStar(start, max_x, max_y, end_x, end_y, blckLs)

    f = open("output.txt", "w", encoding='utf-8')

    if result != False:
        path = []
        while result is not None:
            path.append([result.x, result.y])
            result = result.previous
        path = path[::-1]
        print(path)
        for el in path:
            f.write(" ".join([str(x) for x in el]))
            f.write("\n")

    else:
        f.write("-1")
