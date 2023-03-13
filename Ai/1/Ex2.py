import numpy as np

FINAL = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 0]]

INITIAL = [[3, 2, 1, 4],
           [5, 0, 11, 8],
           [9, 7, 10, 12],
           [13, 14, 6, 15]]

# this is a function used to find the index of a element in 2D list
def index2D(element, arr):
    arr_np = np.array(arr)
    x, y = np.where(arr_np == element)
    return x[0], y[0]

# this is used to find the Manhattan Distance of an element in 2 different lists
def findManhattanDistance(element, arr1, arr2):
    arr1_y, arr1_x = index2D(element, arr1)
    arr2_y, arr2_x = index2D(element, arr2)

    return abs(arr1_x - arr2_x) + abs(arr1_y - arr2_y)

# total manhattan calculation for every element
def totalManhattanDistance(arr1, arr2):
    sum = 0
    for x in arr1:
        for y in x:
            sum += findManhattanDistance(y, arr1, arr2)
    return sum

# comparing final state and the current one generate a state that has the shortest distance
# by calculating every possible move
def bestCostState(final, arr):
    max_x = len(arr)
    max_y = len(arr[0])
    zero_x, zero_y = index2D(0, arr)

    moves = [move for move in [(zero_x - 1, zero_y), (zero_x, zero_y - 1), (zero_x + 1, zero_y), (zero_x, zero_y + 1)]
             if (move[0] >= 0 and move[0] < max_x) and (move[1] >= 0 and move[1] < max_y)]
    # list that have best distance
    best_arr = [x[:] for x in arr]

    # best number to be moved in the board (2D list)
    best_value = best_arr[moves[0][0]][moves[0][1]]

    best_arr[zero_x][zero_y] = best_value
    best_arr[moves[0][0]][moves[0][1]] = 0
    # min manhattan distance
    min_dist = totalManhattanDistance(final, best_arr)

    # find the best option for every possible move
    for move in moves[1:]:
        temp_arr = [x[:] for x in arr]
        val = temp_arr[move[0]][move[1]]
        temp_arr[zero_x][zero_y] = val
        temp_arr[move[0]][move[1]] = 0
        dist = totalManhattanDistance(FINAL, temp_arr)

        if dist < min_dist:
            best_value = val
            min_dist = dist
            best_arr = [x[:] for x in temp_arr]

    return best_arr, min_dist, best_value

# implement the A Star with a limit (depth limit)
def A_Stare(final, initial, max_level=10):

    # list that contain the number to be moved to solve the puzzle
    moves = []
    i = 0
    # if distance 0  return directly the array
    if totalManhattanDistance(final, initial) == 0:
        return moves

    else:
        while True:
            if i == max_level:
                break
            temp_arr, dis, val = bestCostState(final, initial)
            moves.append(val)
            initial = [x[:] for x in temp_arr]
            print(temp_arr)
            print(dis)
            if dis == 0:
                return moves
            i += 1
        return -1


if __name__ == "__main__":
    print(A_Stare(FINAL, INITIAL, max_level=30))
