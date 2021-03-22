# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 03/09/2018

from collections import deque
from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

def dfs1(s):
    global G, R, visited, stack
    visited[s] = 1
    for u in R[s]:
        if visited[u] == 0:
            dfs1(u) ; visited[u] = 1
    stack.append(s)

def dfs2(s):
    global G, R, visited, stack, scc, scc_label
    stack_ = [s] ; visited[s] = 1
    scc[s] = scc_label
    while len(stack_) != 0:
        u = stack_.pop()
        scc[u] = scc_label
        for v in G[u]:
            if visited[v] == 0:
                stack_.append(v) ; visited[v] = 1
        visited[u] = 1

def solve():
    global G, R, visited, stack, scc, scc_label
    size_G = len(G)
    for u in range(size_G):
        for v in G[u]:
            R[v].append(u)
    stack = []
    for u in range(len(R)):
        if visited[u] == 0:
            dfs1(u)
    scc_label = 0
    scc = [0 for _ in range(size_G)]
    visited = [0 for _ in range(size_G)]
    for u in stack:
        if visited[u] == 0:
            dfs2(u) ; scc_label += 1
    bidirection = [0 for _ in range(size_G)]
    for u in range(size_G):
        for v in G[u]:
            if scc[v] != scc[u]:
                bidirection[scc[v]] += 1
    aux = 0
    for i in range(scc_label):
        if bidirection[i] == 0:
            aux += 1
    return max(aux, scc_label)

def main():
    global G, R, visited, stack
    tc = int(stdin.readline())
    while tc > 0:
        n, m = [int(i) for i in stdin.readline().split()]
        G = [[] for _ in range(n)]
        R = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]
        while m > 0:
            x, y = [int(i) for i in stdin.readline().split()]
            # Los nodos están numerados del 1 al n (1..n)
            G[x - 1].append(y - 1)
            m -= 1
        print(solve())
        tc -= 1

main()
