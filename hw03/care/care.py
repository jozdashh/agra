# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 07/09/2018

from sys import stdin

INF = float('inf')

def dfs(s):
    global G, visited
    last = INF
    stack = [s] ; visited[s] = 1
    ans = 1
    while len(stack) != 0:
        u = stack.pop()
        for v in G[u]:
            if visited[v] == 0:
                stack.append(v)
                visited[v] = 1
        visited[u] = 1
        if len(G[u]) == 0:
            if last == INF:
                last = u
            else:
                if last != INF:
                    return 0
    return ans

def toposort(G):
  ans = list()
  indeg = [ 0 for _ in range(len(G)) ]
  for u in range(len(G)):
    for v in G[u]:
      indeg[v] += 1
  pending = list()
  for u in range(len(G)):
    if indeg[u]==0:
      pending.append(u)
  while len(pending)!=0:
    u = pending.pop()
    ans.append(u)
    for v in G[u]:
      indeg[v] -= 1
      if indeg[v]==0:
        pending.append(v)
  return ans

def solve():
    global G, visited
    path = toposort(G)
    ans = 1
    if len(path) < len(G):
        return 0
    for i in range(len(G)):
        if visited[i] == 0:
            ans = dfs(i)
            if ans == 0:
                return 0
    return ans

def main():
    global G, visited
    n, m = [int(i) for i in stdin.readline().split()]
    while n != 0 or m != 0:
        G = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]
        while m > 0:
            a, b = [int(i) for i in stdin.readline().split()]
            G[a].append(b)
            m -= 1
        print(solve())
        n, m = [int(i) for i in stdin.readline().split()]

main()
