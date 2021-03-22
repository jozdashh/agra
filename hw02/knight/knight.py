# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 19/08/2018

from sys import stdin

def dfs(row, col):
    global grid, visited, R, C, M, N, deltar, deltac
    stack = [(row, col)] ; visited[row][col] = 1
    while len(stack) != 0:
        r, c = stack.pop()
        for x in range(8):
            dr, dc = r + deltar[x], c + deltac[x]
            if 0 <= dr < R and 0 <= dc < C and grid[dr][dc] != -1:
                grid[r][c] += 1
                if visited[dr][dc] == 0:
                    stack.append((dr, dc))
                    visited[dr][dc] = 1
        visited[r][c] = 2

def solve():
    global grid, visited, R, C, M, N, deltar, deltac
    deltar = [-N, -M, -M, -N, N, M, M, N]
    deltac = [-M, -N, N, M, M, N, -N, -M]
    even = odd  = 0
    dfs(0, 0)
    for i in range(R):
        for j in range(C):
            if M == 0 or N == 0 or M == N:
                grid[i][j] //= 2
            if grid[i][j] > 0:
                if grid[i][j] % 2 == 0:
                    even += 1
                else:
                    odd += 1
    return (even + 1, odd) if even == odd == 0 else (even, odd)

def main():
    global grid, visited, R, C, M, N
    tc = int(stdin.readline())
    cc = 1
    while tc > 0:
        R, C, M, N = tuple(map(int, stdin.readline().split()))
        grid = [[0 for _ in range(C)] for _ in range(R)]
        visited = [[0 for _ in range(C)] for _ in range(R)]
        W = int(stdin.readline())
        while W > 0:
            wr, wc = tuple(map(int, stdin.readline().split()))
            grid[wr][wc] = -1
            W -= 1
        even, odd = solve()
        print("Case {0}: {1} {2}".format(cc, even, odd))
        cc += 1
        tc -= 1

main()
