# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 18/09/2018

from sys import stdin, setrecursionlimit
setrecursionlimit(10**4)

def solve(t1, t2):
    return ans1 + ans2 + ans3 + ans4

def get_range(s):
    i = 0
    while s[i] == 'p': i+=1
    j = i
    while s[j] != 'p': j+=1
    return (i, j)


def parse_tree(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s[0]]
    else:
        i, j = get_range(s)
        tree = s[i:j]

def main():
    tc = int(stdin.readline())
    while tc > 0:
        t1 = parse_tree(stdin.readline())
        t2 = parse_tree(stdin.readline())
        print("There are {0} black pixels.".format(solve(t1, t2)))
        tc -= 1

main()








"""
>> para el de quad podriamos hacerlo con true y false, y hacer disyunciones.
Eso ahorra código.
Parsear los arboles y hacer, OR(tree_1, tree_2), y eso devuelve la cantidad
de negros. Algo como eso.
"""

"""
This problem is fairly easy too.
We don't need to create a new tree, the tree is there by itself,
it's already given to us.
inductively, we have to encapsulate each tree as:
root (sub_tree) (sub_tree) (node) (node) ...
With recursion it should be done.

The whole square is (32x32).
So, we have to figure out a way to keep track of the depth of every
node or sub-tree. So that, for example, if we have a single square
with 2 blacks:

[w][b]
[b][w]

(w: white, b:black)
the total about of black pixels is 2*(16*16) == 2(256) == 512 == 1024//2.
That means that for each depth, we divide dimensions by 2.
doing (32x32)//(4k) also works too, k being 1 in this case. Simple enough.

Pretend that we have already figured all that out. (parsing the tree and such)
Then, once we are at the end of any of both trees,
that's when we start comparing blacks with whites and such.

If we have the case (sub_tree) vs (node),
if the node is black, ignore the sub_tree and add the nodes dimensions.
Otherwise, count all the blacks
in the subtree and add it to the global result.

if you have (node) vs (node), do as the problem says
if any node is black, then the whole thing is black
(and you should return the pixel's dimention according to the node's depth)
But if both are white,
then everything is white, and you should return 0.

those are the base cases really. sub_tree vs node
if we have sub_tree vs sub_tree we have to keep going deeper until
we find a node. That's it.

Those are the two cases pretty much.

In the end, the return value should look like this:

return solve(sub_tree1, sub_tree2) + solve(sub_tree3, sub_tree4) ...
that's it four times, since each square can be decomposed in 4 squares.

thats pretty much it. It's really simple.
God i fucking love induction, it does everything for you.
:>
"""
