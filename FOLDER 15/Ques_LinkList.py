class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue_LinkList:
    def __init__(self): #Khởi tạo head dùng cho Linked-List của Queue
        self.head = None
    
    def IsEmpty(self): #Hàm kiểm tra xem mảng có rỗng hay không
        if self.head is None: #điều kiện kiểm tra rỗng
            return #Nếu có thì trả về rỗng
    
    def Enqueue_Begin(self, data): #Thêm phần tử vào đầu
        NewNode = Node(data) #Tạo node mới từ data truyền vào
        if self.IsEmpty(): #Kiểm tra mảng xem có rỗng hay không
            self.head = NewNode #Cho head là NewNode nếu mảng ban đầu rỗng
        else:
            NewNode.next = self.head #Còn nếu không rỗng thì liên kết next của NewNode tới head
            self.head = NewNode #Lúc này head là NewNode, tiếp tục cho head = NewNode để đưa giá trị vào head
        
    def Enqueue(self, data): #Thêm phần tử vào Queue
        NewNode = Node(data) #tạo node mới từ data truyền vào
        CurrentNode = self.head #đặt biến CurrentNode là biến chạy cho head
        if self.head is None: #kiểm tra xem ban đầu head có rỗng hay không
            self.Enqueue_Begin(data) #nếu rỗng thì thực hiện Enqueue_Begin
        else:
            while (CurrentNode.next!= None): #Điều kiện để quét Node từ đầu đến cuối Linked-List
                CurrentNode = CurrentNode.next #Chuyển node bằng cách chuyển next
            CurrentNode.next = NewNode #cho next của node cuối cùng bằng NewNode 
            NewNode.next = None #lúc này NewNode là node cuối nên next sẽ là None

    def Dequeue(self): #Hàm xóa phần tử khỏi Queue
        if self.IsEmpty(): #Kiểm tra ban đầu mảng có rỗng hay không
            return #Nếu có thì rả về None
        else:
            print(self.head.data) #in ra giá trị ban đầu của head 
            self.head = self.head.next #chuyển đổi head thành next, nghĩa là head sẽ là node sau của head đầu tiên

    def First(self): #Hàm Lấy giá trị của head
        if self.IsEmpty(): #Kiểm tra xem ban đầu mảng có rỗng hay không
            return #Nếu có thì trả về None
        else:
            return self.head.data #Trả về giá trị của head
        
        
    def Print_Queue(self): #Hàm dùng để in ra Queue dưới dạng Linked-List
        list = [] #mảng rỗng để chứa các node truyền vào
        CurrentNode = self.head #đặt biến chạy là biến head
        while(CurrentNode): #điều kiện để head chạy từ đầu đến node cuối
            list.append(CurrentNode.data) #chèn data của node vào trong list
            CurrentNode = CurrentNode.next #chuyển Node bằng cách dịch chuyển next của head
        print(list) #in ra list

    

# Queue1 = Queue()
# Queue1.Enqueue(10)
# Queue1.Enqueue(20)
# Queue1.Enqueue(30)
# Queue1.Print_Queue()
# Queue1.Dequeue()
# Queue1.Print_Queue()
# print(Queue1.First())


