# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 03/09/2018

from collections import deque
from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

def dfs1(s):
    global G, R, visited, queue
    visited[s] = 1
    for u in R[s]:
        if visited[u] == 0:
            dfs1(u) ; visited[u] = 1
    queue.appendleft(s)
    return

def dfs2(s):
    global G, R, visited, queue, scc, scc_label
    stk = [s] ; visited[s] = 1
    scc[s] = scc_label
    while len(stk) != 0:
        u = stk.pop()
        visited[u] = 1
        scc[u] = scc_label
        for v in G[u]:
            if visited[v] == 0:
                stk.append(v) ; visited[v] = 1

def solve():
    global G, R, visited, queue, scc, scc_label
    queue = deque()
    scc_label = 0
    scc = [0 for _ in range(len(G))]
    for u in range(len(G)):
        for v in G[u]:
            R[v].append(u)
    visited = [0 for _ in range(len(G))]
    for u in range(len(R)):
        if visited[u] == 0:
            dfs1(u)
    visited = [0 for _ in range(len(G))]
    for u in queue:
        if visited[u] == 0:
            dfs2(u) ; scc_label += 1
    bidirection = [0 for _ in range(len(G))]
    for u in range(len(G)):
        for v in G[u]:
            if scc[v] != scc[u]:
                bidirection[scc[v]] += 1
    aux = 0
    for i in range(scc_label):
        if bidirection[i] == 0:
            aux += 1
    # return max(aux, scc_label)
    return aux

def main():
    global G, R
    tc = int(stdin.readline())
    k = 1
    while tc > 0:
        n, m = [int(i) for i in stdin.readline().split()]
        G = [[] for _ in range(n)]
        R = [[] for _ in range(n)]
        while m > 0:
            x, y = [int(i) for i in stdin.readline().split()]
            # Los nodos están numerados del 1 al n (1..n)
            G[x - 1].append(y - 1)
            m -= 1
        print("Case {0}: {1}".format(k, solve()))
        # Espacio vacio entre casos de prueba
        stdin.readline()
        k += 1
        tc -= 1

main()
