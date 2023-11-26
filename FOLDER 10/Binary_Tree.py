from Ques_Array import Queues_Array

class Node:
    __slot__ = 'element', 'left', 'right'
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.left = left 
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def MakeTree(self, e, left, right):
        self.root = Node(e, left.root, right.root)
    
    def InOrder(self, troot):
        if troot:
            self.InOrder(troot.left)
            print(troot.element, end=" ")
            self.InOrder(troot.right)
    
    def PreOrder(self, troot):
        if troot:
            print(troot.element, end=' ')
            self.PreOrder(troot.left)
            self.PreOrder(troot.right)
    
    def PostOrder(self, troot):
        if troot:
            self.PostOrder(troot.left)
            self.PostOrder(troot.right)
            print(troot.element, end=" ")
    
    def LevelOrder(self, troot):
        Q = Queues_Array()
        t = self.root
        print(t.element, end=" ")
        Q.Enqueue(t)
        while not Q.IsEmpty():
            t = Q.Dequeue()
            if t.left:
                print(t.left.element, end=' ')
                Q.Enqueue(t.left)
            if t.right:
                print(t.right.element, end=' ')
                Q.Enqueue(t.right)
    def Count(self, troot):
        if troot:
            x = self.Count(troot.left)
            y = self.Count(troot.right)
            return x + y + 1
        return 0
    
    def Height(self, troot):
        if troot:
            x = self.Height(troot.left)
            y = self.Height(troot.right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0
    
    

    
x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
a = BinaryTree()
t = BinaryTree()
s = BinaryTree()
r = BinaryTree()
x.MakeTree(20, a, a)
y.MakeTree(30, a, a)
z.MakeTree(10, x, y)
r.MakeTree(50, a, y)
s.MakeTree(30, r, a)
z.InOrder(z.root)
print()
z.PreOrder(z.root)
print()
z.PostOrder(z.root)
print()
z.LevelOrder(z.root)
print()
t.MakeTree(10, z, s)
print(z.Count(z.root))
print()
print(t.Height(t.root)-1)




