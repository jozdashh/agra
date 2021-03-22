# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 23/09/2018

from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10 ** 4)

INPUT, I = stdin.buffer.read(), 0
SPACE, CR, LPAR, RPAR, ZERO, NINE, MINUS = ord(' '), ord('\n'), ord('('), ord(')'), ord('0'), ord('9'), ord('-')

def has_next(): return I < len(INPUT)

def is_digit(): return ZERO <= INPUT[I] <= NINE

def is_minus(): return INPUT[I] == MINUS

def read_blanks():
    global INPUT, I
    while has_next() and (INPUT[I] == CR or INPUT[I] == SPACE): I += 1

def read_par():
    global INPUT, I
    ans, I = chr(INPUT[I]), I + 1
    return ans

def read_num():
    global INPUT, I
    ans = 0
    while has_next() and is_digit():
        ans, I = (INPUT[I] - ZERO) + ans*10, I + 1
    return ans

def next_token():
    global INPUT, I
    ans = None
    read_blanks()
    if I != len(INPUT):
        if is_minus():
            I += 1
            ans = read_num()*(-1)
        elif is_digit():
            ans = read_num()
        else: ans = read_par()
    return ans

def solve(i, tkn):
    nxt1, nxt2 = next_token(), next_token() # left par, next number
    if nxt2 != ')': # Not end of branch or empty node
        ltree, rtree = solve(i + nxt2, tkn), solve(i + nxt2, tkn); next_token()
        if ltree == -1 and rtree == -1:
            return 1 if i + nxt2 == tkn else False
        elif ltree == 1 or rtree == 1:
            return True
    else:
        return -1

def main():
    global INPUT, I
    tkn = next_token()
    while tkn != None:
        ans = solve(0, tkn)
        print("yes") if ans == True and ans != -1 else print("no")
        tkn = next_token()

main()


# def main():
#     global INPUT, I
#     tkn = next_token()
#     while tkn != None:
#         ans = solve(0, tkn)
#         print("yes") if ans else print("no")
#         tkn = next_token()
