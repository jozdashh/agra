# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 28/09/2018

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 4)

class BinTree(object):
    def __init__(self, num, left = None, right = None):
        self.num = num
        self.l = left
        self.r = right
        return
    def __str__(self):
        str_l = str(self.l) if self.l != None else ""
        str_r = str(self.r) if self.r != None else ""
        s = "{0} ({1}) ({2})".format(self.num, str_l, str_r)
        return s

def parse(line):
    l = line.split()
    s = list()
    ans = BinTree(None)
    s.append(ans)
    t = ans
    for i in l:
        if i == '(':
            t.l = BinTree(None)
            s.append(t)
            t = t.l
        elif i not in ['+', '-', '*', '/', ')']:
            t.num = float(i)
            p = s.pop()
            t = p
        elif i in ['+', '-', '*', '/']:
            t.num = i
            t.r = BinTree(None)
            s.append(t)
            t = t.r
        elif i == ')':
            t = s.pop()
    return ans

def solve(tree):
    if tree.l == None and tree.r == None:
        return tree.num
    elif tree.num == '+':
        return solve(tree.l) + solve(tree.r)
    elif tree.num == '-':
        return solve(tree.l) - solve(tree.r)
    elif tree.num == '*':
        return solve(tree.l) * solve(tree.r)
    elif tree.num == '/':
        return solve(tree.l) / solve(tree.r)

def main():
    tc = int(stdin.readline())
    while tc > 0:
        ans = round(solve(parse(stdin.readline())), 2)
        print(ans if str(ans)[-3] == '.' else str(ans) + '0')
        tc -= 1

main()
