import collections

class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict

#DEPTH FIRST SEARCH
# Check for the visited and unvisited nodes
def dfs(graph, start, visited = None):
   if visited is None:
      visited = set()
   visited.add(start)
   print(start)
   for next in graph[start] - visited:
      dfs(graph, next, visited)
   return visited


#BREADTH FIRST SEARCH
def bfs(graph, startnode):
# Track the visited and unvisited nodes using queue
   seen = set([startnode])
   queue = collections.deque([startnode])
   while queue:
      vertex = queue.popleft()
      print(vertex, end=' ')
      for node in graph[vertex]:
         if node not in seen:
            seen.add(node)
            queue.append(node)



# The graph dictionary
gdict = {
   "a" : set(["b","c"]),
   "b" : set(["a", "d"]),
   "c" : set(["a", "d"]),
   "d" : set(["e"]),
   "e" : set(["f"]),
   "f" : set()
}

# re = dfs(gdict, 'f')
bfs(gdict, "a")
# print('re',re)
d = {2:1, 3:2, -1:9}
print(max(d))