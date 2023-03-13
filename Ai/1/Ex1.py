# current state and how are elements of 2D array connected
graph = {
    1: [4, 2],
    2: [5, 3, 1],
    3: [6, 2],
    4: [7, 5, 1],
    5: [8, 6, 4, 2],
    6: [9, 5, 3],
    7: [8, 4],
    8: [9, 7, 5],
    9: [8, 6]
}
# linear representation
array = [1, 0, 1, 0, 1, 1, 0, 1, 0]

visited = []

# a dict that keep track of previous state of the list
parent_child = {}

# node is the initial state
def BFS(visited, graph, node, array, parent_child):
    # state after specific flipping
    state = {}
    queue = []

    visited.append(node)
    # frontier of the BFS
    queue.append(node)

    while queue:
        m = queue.pop(0)
        if (m == node):

            # change the value at m-1 as long as list start from 0
            array[m - 1] = 0 if array[m - 1] == 1 else 1

            # flip the other neighbors position
            for x in graph[m]:
                array[x - 1] = 0 if array[x - 1] == 1 else 1
            state[m] = array
        else:
            # other wise make a copy of the list from the parent of this node
            # and make necessary flipping for specified position
            arr = state[parent_child[m]].copy()
            arr[m - 1] = 0 if arr[m - 1] == 1 else 1

            for x in graph[m]:
                arr[x - 1] = 0 if arr[x - 1] == 1 else 1
            state[m] = arr

            # print(state[m])
        # check if all values are turned to one and return the value
        if (sum(state[m]) == 9):
            return m

        # add to queue all adjustment if are not visited
        for el in graph[m]:
            if el not in visited:
                # keep track of previous move that lead to this one
                parent_child[el] = m
                visited.append(el)
                queue.append(el)

    return False

# from the dict that keep track of moves previous and current (parent child)
# specify end and start and find the shortest path within the length of parent_child dict
def shortestPath(parent_child, end, start):
    arr = [end]
    length = len(parent_child.keys())
    i = 0
    while True:
        i += 1
        end = parent_child[end]
        arr.append(end)
        if (end == start):
            break
        if (i > length):
            return False
            break
    return arr


def main():
    i = BFS(visited, graph, 1, array, parent_child)

    if (i != False):
        path = shortestPath(parent_child, i, 1)
        print(len(path))
        print(path[::-1])
    else:
        print("No solution was found")


if __name__ == "__main__":
    main()
