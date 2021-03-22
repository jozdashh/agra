import sys
sys.setrecursionlimit(1000001)

def dfs(v):
    global marked,idi,preorder,pre,c,s,p,G
    marked[v] = 1
    preorder[v] = pre
    pre += 1
    s.append(v);p.append(v)
    for i in G[v]:
        if(marked[i] == 0):
            dfs(i)
        elif(idi[i] == -1):
            while(preorder[p[len(p)-1]] > preorder[i]):
                p.pop()
    if (p[len(p)-1] == v):
        p.pop()
        i = s.pop()
        idi[i] = c
        while(i != v):
            i = s.pop()
            idi[i] = c
        c += 1

def main():
    global marked,idi,preorder,pre,c,s,p,G
    n = 7
    G = [[] for _ in range(n)]
    marked = [0 for _ in range(n)]
    idi = [-1 for _ in range(n)]
    preorder = [0 for _ in range(n)]
    c = 0
    pre = 0
    s,p = [],[]
    for i in range(n):
        if(marked[i] == 0):
            dfs(i)

main()
