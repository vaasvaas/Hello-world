#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def Run():
    f = open("1")
    A=[]
    tree=[]
    for i in f:
        A.append(i.strip().split())
    n = int(A[0][0])
    for k in range(1, n+1):
        a, b, c = A[k]
        tree.append([int(a),int(b),int(c)])
    print(n)
    print("Tree", tree)
    print("----------------------------")
    return tree

def TrueRun():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
      tree.append(list(map(int, sys.stdin.readline().strip().split())))
  return tree

def inOrderRec(A, tree, List):
    if A!=-1:
        if tree[A][1]==-1 and tree[A][2]==-1:

            #if tree[A][0]<List[-1]:
            #    raise IndexError
            return List.append(tree[A][0])
        else:
            inOrderRec(tree[A][1], tree, List)
            #if tree[A][0]<List[-1]:
            #    raise IndexError
            List.append(tree[A][0])
            inOrderRec(tree[A][2], tree, List)


def IsBinarySearchTree(tree):
        List=[]
        if len(tree)!=0:
            inOrderRec(0, tree, List)
            #print(List)
            z=-9999999999999999999999
            for i in List:
                if i<z:
                    return False
                z=i

            return True
        else:
            return True





def main():
  #tree = Run()
  tree=TrueRun()



  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()


