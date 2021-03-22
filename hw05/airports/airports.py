# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 17/10/2018

from sys import stdin

class dforest(object):
  """implements an union-find with path-compression and ranking"""

  def __init__(self, size=10):
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 1 for _ in range(size) ]
    self.__csize = [ 1 for _ in range(size) ]
    self.__ccount = self.__size = size

  def __str__(self):
    """return the string representation of the forest"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return self.__size

  def csize(self, x):
    """return the number of elements in the component of x"""
    return self.__csize[self.find(x)]

  def ccount(self):
    """return  the number of components"""
    return self.__ccount

  def find(self, x):
    """return the representative of the component of x"""
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]

  def union(self, x, y):
    """computes the union of the components of x and y, if they are different"""
    fx,fy = self.find(x),self.find(y)
    if fx!=fy:
      rx,ry = self.__rank[fx],self.__rank[fy]
      if rx>ry:
        self.__parent[fy] = fx
        self.__csize[fx] += self.__csize[fy]
      else:
        self.__parent[fx] = fy
        self.__csize[fy] += self.__csize[fx]
        if rx==ry:
          self.__rank[fy] += 1
      self.__ccount -= 1

def kruskal(graph, lenv):
  ans = list()
  m_cost = 0
  graph.sort(key = lambda x: x[2])
  df,i = dforest(lenv),0
  while i!=len(graph):
    u,v,d = graph[i]
    if df.find(u)!=df.find(v):
      ans.append((u, v, d))
      df.union(u, v)
      m_cost += d
    i += 1
  return (df.ccount(), m_cost)

def main():
    tc = int(stdin.readline())
    tc_p = 1
    while tc > 0:
        n_loc, n_roads, ap_cost = map(int, stdin.readline().split())
        G = list()
        while n_roads > 0:
            u, v, c = map(int, stdin.readline().split())
            if c < ap_cost:
                G.append((u-1, v-1, c))
            n_roads -= 1
        n_ap, road_c = kruskal(G, n_loc)
        m_cost = road_c + n_ap*ap_cost
        print('Case #{0}: {1} {2}'.format(tc_p, m_cost, n_ap))
        tc -= 1
        tc_p += 1

main()
