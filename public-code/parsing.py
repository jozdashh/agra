"""
Esto de acá sí lo hizo rocha lindo
"""

from sys import *
setrecursionlimit(1000000)

INPUT,I = stdin.buffer.read(),0
SPACE,CR,LPAR,RPAR,ZERO,NINE,MINUS = ord(' '),ord('\n'),ord('('),ord(')'),ord('0'),ord('9'),ord('-')

def has_next(): return I<len(INPUT)

def is_par() : return LPAR==INPUT[I] or RPAR==INPUT[I]

def is_digit(): return ZERO <= INPUT[I] <= NINE

def is_minus(): return MINUS==INPUT[I]

def read_blanks():
  global INPUT,I
  while has_next() and not(is_digit()) and not(is_par()) and not(is_minus()): I += 1

def read_par():
  global INPUT,I
  ans,I = chr(INPUT[I]),I+1
  return ans

def signed_num():
  global INPUT,I
  I += 1
  read_blanks()
  return read_num()*-1

def read_num():
  global INPUT,I
  ans = 0
  while has_next() and is_digit(): ans,I = int(chr(INPUT[I]))+ans*10,I+1
  return ans

def next_token():
  global INPUT,I
  ans = None
  read_blanks()
  if I!=len(INPUT):
    if is_digit():
      ans = read_num()
    elif is_minus():
      ans = signed_num()
    else: ans = read_par()
  return ans

def parse_tree():
  ans = list()
  next_token()
  tk = next_token()
  if tk!=')':
    ans.append(tk)
    ans.append(parse_tree())
    ans.append(parse_tree())
    next_token()
  return ans







"""
Ésto de acá abajo fue lo que saqué de la página hermosa de éste tipo todo
extraño. Si buscas "parse binary tree mathematical expression" te sale, es un blog.
"""
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.postorder()  #defined and explained in the next section
