# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 12/08/2018


# Algortimo hecho por el profesor Camilo Rocha en clase


from sys import stdin

board, lenr, lenc = None, None, None
deltar = [ -1, -1, -1, 0, 0, 1, 1, 1 ]
deltac = [ -1, 0, 1, -1, 1, -1, 0, 1 ]
visited = None

def dfs(row, col):
    global visited, lenb
    stack = [ (row, col) ] ; visited[row][col] = 1
    while len(stack) != 0:
        r, c = stack.pop()
        for i in range(len(deltar)):
            dr, dc = r + deltar[i], c + deltac[i]
            if ((0 <= dr < lenb) and (0 <= dc < lenb) and (board[dr][dc] == '1') and not visited[dr][dc]):
                stack.append((dr, dc))
                visited[dr][dc] = 1
        visited[r][c] = 2


def solve():
    global board, lenr, lenc, visited, lenb
    visited = [ [0 for _ in range(lenb)] for _ in range(lenb) ]
    ans = 0
    for r in range(lenb):
        for c in range(lenb):
            if board[r][c] == '1' and visited[r][c] == 0:
                ans += 1
                dfs(r, c)
    return ans

def main():
    global board, lenr, lenc, lenb
    tc = 1
    line = stdin.readline()
    while len(line) != 0:
        lenb = int(line)
        board = list()
        for i in range(lenb):
            board.append(stdin.readline().strip())
        print("Image number {0} contains {1} war eagles.".format(tc, solve()))
        line = stdin.readline()
        tc += 1

main()
