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

# Arbol en pre-order
# [3, [2, 10, 7], [4, 3, 9]]

a = BinTree(3, None, None)
a.l = BinTree(2, BinTree(10), BinTree(7))
a.r = BinTree(4, BinTree(3), BinTree(9))
print(a)

# Ahora, vamos a hacer una función que imprima la lista de listas
# mostrada arriba (en In-Order)

b = [3, [2, 10, 7], [4, 3, 9]]
def print_tree(x):
    if type(x) != list:
        print(x, end = '') if x != None else print()
    else:
        print("(", end = '')
        print_tree(x[1])
        print(") ", end = '')

        print(x[0], end = '')

        print(" (", end = '')
        print_tree(x[2])
        print(")", end = '')

print_tree(b) ; print()


# Ahora, vamos a ver una representación de un arbol binario
# usando un solo arreglo
# i : index
# parent(i) = i // 2
# left(i) = 2 * i
# right(i) = 2 * i + 1

# Eso si enumaramos cada nodo como 1..n.
# Si lo hacemos como 0..n:
# parent(i) = ((i + 1) // 2) - 1
# left(i) = 2 * (i + 1) - 1
# right(i) = 2 * (i + 1) + 1 - 1

c = ['?', 3, 2, 4, 10, 7, 4, 9] # Esto es usando la enumeracion 1..n

# r: root
def print_tree_arr(x, r):
    print("(", end = '')
    if 2*r < len(x):
        print_tree_arr(x, 2*r)
    print(") ", end = '')

    print(x[r], end = '')

    print(" (", end = '')
    if 2*r + 1 < len(x):
        print_tree_arr(x, 2*r + 1)
    print(")", end = '')

print_tree_arr(c, r = 1) ; print()
