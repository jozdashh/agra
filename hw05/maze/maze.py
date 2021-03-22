# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 10/10/2018

from heapq import heappop, heappush
from sys import stdin

INF = float('inf')

def dijkstra(G, s, t):
    ans = [INF for _ in G]
    ans[s] = 0
    visited = [False for _ in G]
    heap = [(0, s)]
    while len(heap) != 0:
        du, u = heappop(heap)
        if visited[u] == False:
            for v, dv in G[u]:
                if du + dv < ans[v]:
                    ans[v] = du + dv
                    heappush(heap, (ans[v], v))
            visited[u] = True
    ct = 0
    for d in ans:
        if d <= t:
            ct += 1
    return ct

def main():
    tc = int(stdin.readline())
    while tc > 0:
        stdin.readline()
        n = int(stdin.readline())
        G = [list() for _ in range(n)]
        exit = int(stdin.readline()) - 1
        t = int(stdin.readline())
        m = int(stdin.readline())
        while m > 0:
            a, b, d = map(int, stdin.readline().split())
            # We traspose the graph
            G[b - 1].append((a - 1, d))
            m -= 1
        print(dijkstra(G, exit, t))
        tc -= 1
        if tc != 0:
            print('')

main()
