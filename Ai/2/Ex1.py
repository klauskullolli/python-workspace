from queue import Queue
# function to determine the edge colors
def colorEdges(ptr, gra, edgeColors, isVisited):
  q=Queue()
  c = 0

  colored=set()

  # return if isVisited[ptr] is true
  if (isVisited[ptr]):
    return

  # Mark the current node visited
  isVisited[ptr] = True

  # Traverse all edges of current vertex
  for i in range(len(gra[ptr])) :
    # if already colored, insert it into the set
    if (edgeColors[gra[ptr][i][1]] != -1):
      colored.add(edgeColors[gra[ptr][i][1]])
  

  for i in range(len(gra[ptr])) :
    # if not visited, inset into the queue
    if not isVisited[gra[ptr][i][0]]:
      q.put(gra[ptr][i][0])

    if (edgeColors[gra[ptr][i][1]] == -1) :
      # if col vector -> negative
      while c in colored:

        # increment the color
        c+=1

      # copy it in the vector
      edgeColors[gra[ptr][i][1]] = c

      # then add it to the set
      colored.add(c)
      c+=1
    
  

  # while queue's not empty
  while not q.empty() :
    temp = q.get()

    colorEdges(temp, gra, edgeColors, isVisited)
  

  return


# Driver Function
if __name__=='__main__':
  empty=set()

  # declaring vector of vector of pairs, to define Graph
  gra=[]

  edgeColors=[]

  isVisited=[False]*100000

  # Enter the Number of Vertices
  # and the number of edges
  ver = 4
  edge = 4

  gra=[[] for _ in range(ver)]
  edgeColors=[-1]*edge

  # Enter edge & vertices of edge
  # x-- y--
  # Since graph is undirected, push both pairs
  # (x, y) and (y, x)
  # graph[x].append((y, i))
  # graph[y].append((x, i))
  gra[0].append((1, 0))
  gra[1].append((0, 0))

  gra[1].append((2, 1))
  gra[2].append((1, 1))

  gra[2].append((3, 2))
  gra[3].append((2, 2))

  gra[0].append((3, 3))
  gra[3].append((0, 3))

  colorEdges(0, gra, edgeColors, isVisited)

  # printing all the edge colors
  for i in range(edge):
    print("Edge {} is of color {}".format(i + 1,edgeColors[i] + 1))