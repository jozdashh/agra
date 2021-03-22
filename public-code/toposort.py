def toposort(G):
  """Generates a topological sorting of the graph G, given in adjacency
  list representation. If the returned list does not have all
  vertices, then there is not a topological sorting of G
  """
  # ans will keep track of the sorting of the vertices
  ans = list()
  # compute the in degree of all vertices in G
  indeg = [ 0 for _ in range(len(G)) ]
  for u in range(len(G)):
    for v in G[u]:
      indeg[v] += 1
  # keep track of the vertices with in-degree 0 that have not been
  # assigned in the ordering of the vertices
  pending = list()
  for u in range(len(G)):
    if indeg[u]==0:
      pending.append(u)
  # while there are vertices with in-degree 0, keep generating the
  # topological sorting of the vertices
  while len(pending)!=0:
    u = pending.pop()
    ans.append(u)
    for v in G[u]:
      indeg[v] -= 1
      if indeg[v]==0:
        pending.append(v)
  return ans
