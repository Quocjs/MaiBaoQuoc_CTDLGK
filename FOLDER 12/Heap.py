class Heap:
    def __init__(self):
        self.maxsize = 10
        self.data = [-1]*self.maxsize
        self.csize = 0
    
    def __len__(self):
        return len(self.data)
    
    def IsEmpty(self):
        return len(self.data)
    
    def Insert(self, e):
        if self.csize == self.maxsize:
            print("No Space in Heap")
            return 
        self.csize = self.csize + 1
        hi = self.csize
        while hi > 1 and e > self.data[hi // 2]:
            self.data[hi] = self.data[hi // 2]
            hi = hi // 2
        self.data[hi] = e
    
    def max(self):
        if self.csize == 0:
            print("Heap is Empty")
            return 
        return self.data[1]

    def DeleteMax(self):
        if self.csize == 0:
            print("Heap is empty")
            return 
        e = self.data[1]
        self.data[1] = self.data[self.csize]
        self.data[self.csize] = -1
        self.csize = self.csize - 1
        i = 1
        j = i * 2
        while j <= self.csize:
            if self.data[j] < self.data[j+1]:
                j = j + 1
            if self.data[i] < self.data[j]:
                temp = self.data[i]
                self.data[i] = self.data[j]
                self.data[j] = temp
                i = j
                j = i * 2
            else:
                break
        return e
   
S = Heap()
S.Insert(25)
S.Insert(14)
S.Insert(2)
S.Insert(20)
S.Insert(10)
print(S.data)
S.Insert(40)
print(S.data)
print(S.DeleteMax())
print(S.data)




