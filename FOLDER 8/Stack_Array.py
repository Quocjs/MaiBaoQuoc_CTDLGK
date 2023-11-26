#Xây dựng Stack bằng array

#Các công cụ cơ bản của 1 stack:
# isempty(): kiểm tra mảng có rỗng hay không
# push(): thêm phần tử mới vào stack
# pop(): đẩy phần tử được thêm vào gần nhất của stack
# top(): sử dụng phần tử được thêm vào gần nhất của stack -> không đẩy đi

class Stack_Array:
    def __init__(self): #hàm khởi tạo object của mảng
        self.data = []
    def __len__(self): #hàm khởi tạo chiều dài của mảng
        return len(self.data)
    
    def IsEmpty(self): #hàm kiểm tra mảng có rỗng hay không
        return len(self.data) == 0 #trả về kích thước của array
    
    def Push(self, e): #hàm thêm phần tử mới vào stack
        self.data.append(e) #thêm element mới vào trong stack

    def Pop(self): #hàm xóa phần tử được thêm vào gần nhất của stack
        if (self.IsEmpty()): #kiểm tra mảng có rỗng hay không
            print("Mảng này rỗng")
        return self.data.pop() #thực hiện xóa phần tử gần nhất đó
    
    def Top(self): #hàm lấy, hoặc sử dụng phần tử được thêm vào gần nhất của stack
        if (self.IsEmpty()): #kiểm tra mảng có rỗng hay không
            print("Mảng này rỗng")
        return self.data[-1] #thực hiện lấy phần tử được thêm gần nhất, tức là phần tử cuối cùng
    
S = Stack_Array()
S.Push(4)
S.Push(6)
S.Push(8)
print(S.data)
print("Kích thước của Mảng ban đầu là:",len(S.data))
S.Pop()
print(S.data)
print("Kích thước của Mảng sau khi sử dụng pop:",len(S.data))
a = S.Top()
print("Phần tử được lấy là", a)
S.Pop()
print(S.data)
S.Pop()
print(S.data)
print(S.IsEmpty())




    



    

