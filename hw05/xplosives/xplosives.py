# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 12/10/2018

from heapq import heappop, heappush
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
    """return  the numnber of components"""
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

def main():
    line = stdin.readline()
    while line != '':
        forest = dforest(10**5 + 1)
        cnt = 0
        while line != '-1\n':
            u, v = map(int, line.split())
            if forest.find(u) == forest.find(v):
                cnt += 1
            else:
                forest.union(u, v)
            line = stdin.readline()
        print(cnt)
        stdin.readline()
        line = stdin.readline()

main()
