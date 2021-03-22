# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 09/09/2018

from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10 ** 4)

def dfs(s, p):
    global G, n, m, time, disc, low, comp
    children = 0
    disc[s] = low[s] = time
    time += 1
    for v in G[s]:
        if disc[v] == -1:
            dfs(v, s)
            children += 1
            if low[v] >= disc[s]:
                comp[s] = children - 1 if s == p else comp[s] + 1
            low[s] = min(low[s], low[v])
        elif v != p:
            low[s] = min(low[s], disc[v])

def solve():
    global G, n, m, time, disc, low, comp
    time = 0
    for i in range(n):
        if disc[i] == -1:
            dfs(i, i)
    stations = [-1 for _ in range(n)]
    for i in range(n):
        stations[i] = i
    stations.sort(key=lambda x : x)
    stations.sort(key=lambda x : comp[x], reverse = True)
    for i in range(m):
        print(stations[i], comp[stations[i]] + 1)

def main():
    global G, n, m, disc, low, comp
    n, m = [int(x) for x in stdin.readline().split()]
    while n != 0 and m != 0:
        G = [[] for _ in range(n)]
        disc = [-1 for _ in range(n)]
        low = [0 for _ in range(n)]
        comp = [0 for _ in range(n)]
        x, y = [int(x) for x in stdin.readline().split()]
        while x != -1 and y != -1:
            G[x].append(y)
            G[y].append(x)
            x, y = [int(x) for x in stdin.readline().split()]
        solve()
        n, m = [int(x) for x in stdin.readline().split()]
        if n != 0 and m != 0:
            print("")

main()
