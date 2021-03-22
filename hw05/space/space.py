# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 13/10/2018

from sys import stdin

deltar = [0, -1, 0, 1]
deltac = [-1, 0, 1, 0]

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
      return self.__csize[self.find(x)]
    """return the number of elements in the component of x"""

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
        r, c, s = map(int, line.split())
        forest = dforest(r*c + 2)
        up, dw = [0 for _ in range(c)], [r for _ in range(c)]
        cnt = 0
        for _ in range(r):
            row = stdin.readline()
            for cell in range(len(row)):

        for _ in range(s):
            pass

main()

# Nah parce. Pailas. No voy a hacer éste problema.
