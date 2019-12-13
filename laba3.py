def createMatrix(V, G):
     matrix = []

     for i in range(0, V):
         matrix.append([])
         for j in range(0, V):
             matrix[i].append(0)

     for i in range(0, len(G)):
         matrix[G[i][0]][G[i][1]] = G[i][2]
         matrix[G[i][1]][G[i][0]] = G[i][2]
     return matrix

#Алгоритм Прима
def primAlgorithm(V, G):
     matrix = createMatrix(V, G)
     vertex = 0
     minWay = []
     edges = []
     visited = []
     minEdge = [None, None, float('inf')]

     while len(minWay) != V - 1:
         visited.append(vertex)

         for r in range(0, V):
             if matrix[vertex][r] != 0:
                 edges.append([vertex, r, matrix[vertex][r]])

         for e in range(0, len(edges)):
             if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
                 minEdge = edges[e]

         edges.remove(minEdge)

         minWay.append(minEdge)

         vertex = minEdge[1]
         minEdge = [None, None, float('inf')]

     return minWay

graph = [
     [1, 1, 7],
     [1, 3, 5],
     [1, 4, 3],
     [0, 5, 8],
     [0, 5, 9],
     [2, 5, 10],
     [2, 7, 6],
     [3, 5, 7],
     [3, 6, 6],
     [4, 6, 10],
     [4, 7, 6],
     [5, 7, 3],
     [6, 7, 4]
 ]
print("Prim's algorithm: ")
print(primAlgorithm(8, graph))


class Graph:
     def init(self, vertices):
         self.V = vertices
         self.graph = []

     def addEdge(self, u, v, w):
         self.graph.append([u, v, w])

     def find(self, parent, i):
         if parent[i] == i:
             return i
         return self.find(parent, parent[i])

     def union(self, parent, rank, x, y):
         xRoot = self.find(parent, x)
         yRoot = self.find(parent, y)
         if rank[xRoot] < rank[yRoot]:
             parent[xRoot] = yRoot
         elif rank[xRoot] > rank[yRoot]:
             parent[yRoot] = xRoot
         else:
             parent[yRoot] = xRoot
             rank[xRoot] += 1

    #Алгоритм Краскава
     def kraskavAlgorithm(self):
         result = []
         i, e = 0, 0
         self.graph = sorted(self.graph, key=lambda item: item[2])
         parent = []
         rank = []
         for node in range(self.V):
             parent.append(node)
             rank.append(0)
         while e < self.V - 1:
             u, v, w = self.graph[i]
             i = i + 1
             x = self.find(parent, u)
             y = self.find(parent, v)
             if x != y:
                 e = e + 1
                 result.append([u, v, w])
                 self.union(parent, rank, x, y)
         print("\nKraskav's algorithm: ")
         print("Vertex 'A'   Vertex 'B'  Weight")
         for u, v, weight in result:
             print("%5d %9d %10d" % (u, v, weight))


graph = Graph(8)
graph.addEdge(0, 1, 7)
graph.addEdge(0, 3, 5)
graph.addEdge(0, 4, 3)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 5, 9)
graph.addEdge(2, 5, 10)
graph.addEdge(2, 7, 6)
graph.addEdge(3, 5, 7)
graph.addEdge(3, 6, 6)
graph.addEdge(4, 6, 10)
graph.addEdge(4, 7, 6)
graph.addEdge(5, 7, 3)
graph.addEdge(6, 7, 4)
graph.kraskavAlgorithm()
