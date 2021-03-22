# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 24/08/2018

from sys import stdin

deltar = [0, -1, 0, 1]
deltac = [-1, 0, 1, 0]

def dfs(row, col):
    global N, board, visited
    stack = [(row, col)] ; visited[row][col] = True
    counter = 1
    while len(stack) != 0:
        r, c = stack.pop()
        for i in range(4):
            dr, dc = r + deltar[i], c + deltac[i]
            if 0 <= dr < N and 0 <= dc < N and board[dr][dc] == board[r][c] and not visited[dr][dc]:
                stack.append((dr, dc))
                visited[dr][dc] = True
                counter += 1
        visited[r][c] = True
    return counter

def solve():
    global N, board, revised, visited
    for i in range(N):
        for j in range(N):
            if revised[board[i][j]] == 0:
                revised[board[i][j]] += dfs(i, j)
    ans = "good"
    i = 0
    while i < len(revised) and ans == "good":
        if revised[i] != N:
            ans = "wrong"
        i += 1
    return ans

def main():
    global N, board, revised, visited
    N = int(stdin.readline())
    while N != 0:
        # El último grupo (n - 1) queda marcado con 0's en board.
        board = [[0 for _ in range(N)] for _ in range(N)]
        visited = [[False for _ in range(N)] for _ in range(N)]
        # La posición 0 corresponde a la (n - 1) en éste arreglo
        revised = [0 for _ in range(N)]
        auxN = N - 1
        label = 1
        while auxN > 0:
            aux = list(map(int, stdin.readline().split()))
            aux1, aux2 = list(), list()
            for i in range(0, len(aux), 2):
                aux1.append(aux[i] - 1)
            for i in range(1, len(aux), 2):
                aux2.append(aux[i] - 1)
            for (i, j) in zip(aux1, aux2):
                board[i][j] = label
            label += 1
            auxN -= 1
        print(solve())
        try:
            N = int(stdin.readline())
        except ValueError:
            pass
main()
