from LinkedList import LinkedList
class HashChain:

    #Hàm khởi tạo đối tượng HashChain. 
    def __init__(self):
        self.hashtable_size = 10 #đặt kích thước Hash Table thành 10, 
        self.hashtable = [0]*self.hashtable_size
        # Tạo một bảng Hash trống và khởi tạo mỗi phần tử của bảng băm thành một đối tượng LinkedList.
        for i in range(self.hashtable_size):
            self.hashtable[i] = LinkedList() 
    
    #Hàm Hash cho một khóa cho trước 
    def hashcode(self, key):
        return key %self.hashtable_size #Sử dụng toán tử modulo (%) để phân phối các khóa đồng đều trên hash table.
    
    # Hàm chèn một phần tử vào hash table
    def insert(self, element):
        i = self.hashcode(element) #tính hàm băm cho phần tử, sau đó chèn phần tử vào LinkedList tương ứng. 
        self.hashtable[i].insertionsorted(element)#LinkedList sử dụng thuật toán insertionsorted để giữ cho các phần tử được sắp xếp.
    
    # Hàm tìm kiếm một phần tử trong hash table. 
    def search(self, key):
        # tính hàm hash cho key, sau đó gọi phương thức search trên LinkedList tương ứng.
        i = self.hashcode(key)
        # Phương thức search trả về True nếu tìm thấy phần tử và False nếu không.
        return self.hashtable[i].search(key) != -1
    
    #Hàm hiển thị hash table. 
    def display(self):
        for i in range(self.hashtable_size):
            print('[',i,']', end =' ') #in chỉ số của phần tử và nội dung của LinkedList tương ứng.
            self.hashtable[i].display()
        print()

H = HashChain()
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)
H.insert(34)
H.insert(86)
H.insert(28)

H.display()
print("Result", H.search(54))


