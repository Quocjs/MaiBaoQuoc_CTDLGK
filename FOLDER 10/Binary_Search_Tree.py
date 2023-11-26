class Node:
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.left = left
        self.right = right
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def RInsert(self, troot, e):
        if troot:
            if e < troot.element:
                troot.left = self.RInsert(troot.left, e)
            elif e > troot.element:
                troot.right = self.RInsert(troot.right, e)
        else:
            n = Node(e)
            troot = n
        return troot

    def Insert(self, troot, e):
        temp = None
        while troot:
            temp = troot
            if e == troot.element:
                return 
            elif e < troot.element:
                troot = troot.left
            elif e > troot.element:
                troot = troot.right
        n = Node(e)
        if self.root:
            if e < temp.element:
                temp.left = n
            else: 
                temp.right = n
        else:
            self.root = n
    
    def Search(self, key):
        troot = self.root
        while troot:
            if key == troot.element:
                return True
            elif key < troot.element:
                troot = troot.left
            elif key > troot.element:
                troot = troot.right
        return False

    def RSearch(self, troot, key):
        if troot:
            if key == troot.element:
                return True
            elif key < troot.element:
                return self.RSearch(troot.left, key)
            elif key > troot.element:
                return self.RSearch(troot.right, key)
        else:
            return False
    
    def Deletion(self, e):
        p = self.root
        pp = None
        while p and p.element != e:
            pp = p
            if e < p.element:
                p = p.left
            else:
                p = p.right
        if not p:
            return False
        if p.left and p.right:
            s = p.left
            ps = p
            while s.right:
                ps = s
                s = s.right
            p.element = s.element
            p = s
            pp = ps
        c = None
        if p.left:
            c = p.left
        else:
            c = p.right
        if p == self.root:
            self.root = None
        else:
            if p == pp.left:
                pp.left = c
            else:
                pp.right = c
 
    def InOrder(self, troot):
        if troot:
            self.InOrder(troot.left)
            print(troot.element, end=' ')
            self.InOrder(troot.right)

B = BinarySearchTree()
B.root = B.RInsert(B.root, 50)
B.RInsert(B.root, 50)
B.RInsert(B.root, 30)
B.RInsert(B.root, 80)
B.RInsert(B.root, 10)
B.RInsert(B.root, 40)
B.RInsert(B.root, 60)
B.InOrder(B.root)
print()
print(B.RSearch(B.root, 60))
print(B)
B.Deletion(60)
B.InOrder(B.root)




