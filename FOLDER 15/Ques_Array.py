class Queues_Array:
    def __init__(self): #Hàm khởi tạo data ở đây dùng []
        self.data = []
    
    def __len__(self): #hàm lấy độ dài của Queue
        return len(self.data) 
    
    def IsEmpty(self): #Hàm kiểm tra mảng có rỗng hay không
        return len(self.data) == 0 #nếu có, thì trả về độ dài của data là 0
    
    def Enqueue(self, e): #Hàm truyền phần tử mới vào trong Queue
        self.data.append(e)
    
    def Dequeue(self): #Hàm đẩy phần tử đầu tiên ra khỏi Queue
        if self.IsEmpty(): #Kiểm tra mảng có rỗng hay không
            print("Queue is empty") #nếu có thì in ra là Queue is Empty
            return
        return self.data.pop(0) #lấy đi phần tử đầu tiên của Queue

    def First(self): #Hàm sử dụng phần tử đầu tiên của Queue
        if self.IsEmpty(): #Kiểm tra mảng có rỗng hay không
            print("Queue is empty") #nếu có thì in ra là Queue is Empty
            return
        return self.data[0] #Sử dụng phần tử đầu tiên của Queue, ở đây sử dụng chỉ số index nên là 0 


# Q = Queues_Array()
# Q.Enqueue(5)
# Q.Enqueue(3)
# print(Q.data)
# print("Length:", len(Q))
# Q.Enqueue(7)
# Q.Enqueue(12)
# print(Q.data)
# print(Q.Dequeue())
# print(Q.data)
# print(Q.First())



