# this is the class that represent a tile in a board
class Tile:
    def __init__(self, id, x, y, length, direction, special):
        self.id = id
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction
        self.special = special

    # create a hard copy, is better if is no reference
    def __copy__(self):
        return Tile(self.id, self.x, self.y, self.length, self.direction, self.special)

    # for comparing 2 tiles object
    def __eq__(self, other):
        if not isinstance(other, Tile):
            return False
        if self.id != other.id:
            return False
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        if self.direction != other.direction:
            return False
        if self.special != other.special:
            return False

        return True


class Board:

    def __init__(self, tiles, path, move):

        # list of tiles in a board
        self.tiles = tiles
        # path that show how is passed form a board format to other format after each move made
        self.path = []
        # used to keep track which is the move made to reach this board format
        self.move = move
        # initialization of game board for each board format it is [6][6]
        self.gboard = [[0] * 6] * 6

        # file the board with id of particular tile in the space where is placed in the board
        for tile in tiles:
            if tile.direction == "H":
                for y in range(tile.y, tile.y + tile.length):
                    self.gboard[tile.x][y] = tile.id
            else:
                for x in range(tile.x, tile.x + tile.length):
                    self.gboard[x][tile.y] = tile.id
        for board in path:
            self.path.append(board)

        path.add(self)

    # entire logic of defining possible moves from the current board and generating others
    def nextPossibleBoards(self):

        possibleBoards = []

        # check each tile
        for i in range(0, len(self.tiles)):

            tile = self.tiles[i]

            # if current tile is horizontally set
            if tile.direction == "H":

                # check if can move left
                if (tile.y > 0) and (self.gboard[tile.x][tile.y - 1] == 0):
                    counter = tile.y

                    # check for the largest left possible movement
                    while counter > 0 and self.gboard[tile.x][counter - 1] == 0:
                        counter -= 1
                    tiles = []

                    # update the current checked tile with the left movement and make copy of others for new created
                    # board
                    for j in range(0, len(self.tiles)):
                        if i == j:
                            tiles.insert(j, Tile(tile.id, tile.x, counter, tile.length, tile.direction, tile.special))
                        else:
                            tiles.insert(j, tile.__copy__())

                    # create move dict to keep track of moves made to reach current board
                    move = {
                        "x": tile.x,
                        "y": tile.y,
                        "displacement": counter,
                        "direction": "L"
                    }
                    possibleBoards.append(Board(tiles, self.gboard, move))

                # check the current tile if can move right
                if (tile.y + tile.length < 6) and self.gboard[tile.x][tile.y + tile.length] == 0:
                    counter = tile.y
                    # check for the largest right possible movement
                    while (counter < 6 - tile.length) and self.gboard[tile.x][counter + tile.length] == 0:
                        counter += 1

                    tiles = []

                    # update the current checked tile with the right movement and make copy of others for new created
                    # board
                    for j in range(0, len(self.tiles)):
                        if i == j:
                            tiles.insert(j, Tile(tile.id, tile.x, counter, tile.length, tile.direction, tile.special))
                        else:
                            tiles.insert(j, tile.__copy__())
                    # create move dict to keep track of moves made to reach new created board
                    move = {
                        "x": tile.x,
                        "y": tile.y,
                        "displacement": counter,
                        "direction": "R"
                    }
                    possibleBoards.append(Board(tiles, self.gboard, move))

            # if current tile is vertically set
            else:
                # check if can move up
                if tile.x > 0 and self.gboard[tile.x - tile.length][tile.y] == 0:

                    counter = tile.x

                    # check for the largest up possible movement
                    while (counter - tile.length) > 0 and self.gboard[counter - 1][tile.y] == 0:
                        counter -= 1

                    tiles = []

                    # update the current checked tile with the up movement and make copy of others for new created
                    # board
                    for j in range(0, len(self.tiles)):
                        if i == j:
                            tiles.insert(j, Tile(tile.id, counter, tile.y, tile.length, tile.direction, tile.special))
                        else:
                            tiles.insert(j, tile.__copy__())

                    # create move dict to keep track of moves made to reach new created board
                    move = {
                        "x": tile.x,
                        "y": tile.y,
                        "displacement": counter,
                        "direction": "U"
                    }
                    possibleBoards.append(Board(tiles, self.gboard, move))

                # # check if can move down
                if (tile.x + tile.length < 6) and self.gboard[tile.x + 1][tile.y] == 0:

                    counter = tile.x

                    # check for the largest down possible movement
                    while (counter < 6) and self.gboard[counter + 1][tile.y] == 0:
                        counter += 1

                    tiles = []

                    # update the current checked tile with the down movement and make copy of others for new created
                    # board
                    for j in range(0, len(self.tiles)):
                        if i == j:
                            tiles.insert(j, Tile(tile.id, counter, tile.y, tile.length, tile.direction, tile.special))
                        else:
                            tiles.insert(j, tile.__copy__())

                    # create move dict to keep track of moves made to reach new created board
                    move = {
                        "x": tile.x,
                        "y": tile.y,
                        "displacement": counter,
                        "direction": "D"
                    }
                    possibleBoards.append(Board(tiles, self.gboard, move))

        return possibleBoards


# this is a method that create dictionary with data fetch from file
def uploadInputData(fileName):
    list_tile = []
    with open(fileName) as f:
        f.readline()
        for line in f:
            input_arr = line.split(" ")
            tile = {
                "direction": input_arr[0],
                "x": int(input_arr[1]),
                "y": int(input_arr[2]),
                "length": int(input_arr[3])
            }
            list_tile.append(tile)
        f.close()
    return list_tile


# check if special tile (blocked one) can move freely
def isWinner(board: Board) -> bool:
    special = None
    for tile in board.tiles:
        if tile.special == True:
            special = tile
            break
    for y in range(special.y, 6):
        if board.gboard[special.x][y] != 0:
            return False

    return True

# use bread first to find the shortest path to solve the puzzle using limit by default settled 20
def BFS(currentBoard: Board, limit=20):
    visited = []
    queue = []
    i = 1
    queue.append(currentBoard)
    while queue:
        board = queue.pop(0)
        if board not in visited:
            visited.append(board)
            if isWinner(board):
                return board.path
            if i == limit:
                break
            for b in board.nextPossibleBoards():
                queue.append(b)

    return None


if __name__ == "__main__":
    data = uploadInputData("input2.txt")
    tiles = []
    tile = Tile(1,data[0]["x"], data[0]["y"], data[0]["length"], data[0]["direction"], True)
    tiles.append(tile)

    # file list of tiles from file data
    for el in data[1:]:
        tiles.append(Tile(1, el["x"], el["y"], el["length"], el["direction"], False))

    # create initial board
    board = Board(tiles, [], None)

    path = BFS(currentBoard=board, limit=30)

    f = open("output2.txt")
    if path is None:
        f.write("-1")
        f.close()
    else:
        for b in path:
            f.write(str(len(path) - 1) + "\n")
            if b.move is not None:
                f.write(str(b.move["x"]) + " " + str(b.move["y"]) + " " + str(b.move["displacement"]) + " " + b.move["direction"] + "\n")
        f.close()

