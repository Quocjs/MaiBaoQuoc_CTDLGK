#Xây dựng Stack bằng Link-List

#Các công cụ cơ bản của 1 stack:
# isempty(): kiểm tra mảng có rỗng hay không
# push(): thêm phần tử mới vào stack
# pop(): đẩy phần tử được thêm vào gần nhất của stack
# top(): sử dụng phần tử được thêm vào gần nhất của stack -> không đẩy đi

class Node:
    def __init__(self, data): #Khởi tạo đơn vị đơn giản nhất của 1 Node là data và next
        self.data = data
        self.next = None

class Stack:
    def __init__(self): #khởi tạo head của Linked-list
        self.head = None
    

    def IsEmpty(self): #Kiểm tra Linked-List có rỗng hay không
        if self.head is None:
            return True #Trả về True nếu Linked-List thực sự rỗng
        return False #Trả về False nếu ngược lại trường hợp trên
    
    
    def Push_Begin(self, data): #Hàm Push Begin nếu muốn thay thế phần tử đầu, hàm này chỉ là hàm phụ nên không quan trọng
        NewNode = Node(data) #Tạo Node mới từ giá trị đưa vào
        if self.head is None: #Kiểm tra mảng có rỗng hay không
            self.head = NewNode #Nếu có thì cho phần tử đầu của Link-List là Node vừa mới khởi tạo
        else:
            NewNode.next = self.head #Nếu không rỗng thì đưa địa chỉ của NewNode trùng với head
            self.head = NewNode #lúc này head đã là NewNode nhưng cần đưa vào để chương trình lấy giá trị của NewNode


    def Push(self, data): #Hàm lấy đẩy giá trị mới vào stack
        NewNode = Node(data) #Tạo Node mới từ giá trị đưa vào
        if self.head is None: #Kiểm tra mảng có rỗng hay không
            self.Push_Begin(data) #Nếu rỗng thì thực hiện hàm phụ Push_Begin(data)
        else:
            CurrentNode =  self.head #Đặt biến chạy CurrentNode là head
            while(CurrentNode.next): #Điều kiện để vòng lặp quét tới Node cuối cùng
                CurrentNode = CurrentNode.next #Dịch chuyển next để sang Node mới
            CurrentNode.next = NewNode #Cho next tiếp theo của Node cuối cùng bằng NewNode
            NewNode.next = None #Kết thúc NewNode bằng None, hiểu đây là phần tử vừa thêm vào cuối nên chính nó là tail
    
    def Length_Stack(self): #Hàm lấy độ dài của Stack
        count = 0 #đặt biến đếm ban đầu là 0
        CurrentNode = self.head #Biến chạy CurrentNode là head
        while(CurrentNode): #điều kiện để head chạy đến được Node cuối cùng
            count = count+1 #Cứ mỗi lần đến được node mới thì đếm lên 1
            CurrentNode = CurrentNode.next #dịch chuyển Node
        print(count) #in ra độ dài của stack


    def Pop(self): #Hàm xóa giá trị cuối cùng của Stack
        if self.head is None: #Kiểm tra Linked-List có rỗng hay không
            return #Trả về None nếu Linked-List thực sự rỗng
        CurrentNode = self.head #Đặt biến CurrentNode làm biến chạy cho head
        while (CurrentNode.next.next != None): #điều kiện để tồn tại Node kế tiếp
            CurrentNode = CurrentNode.next #Thực hiện dịch chuyển 1 Node sang Node tiếp theo
        CurrentNode.next = None #Đưa next của phần tử kề cuối là None thì hoàn toàn xóa được Node cuối cùng

    def Top(self): #Hàm lấy giá trị cuối cùng để sử dụng 
        if self.head is None: #Kiểm tra Linked-List có rỗng hay không
            return  #Nếu có thì trả về None
        else:
            CurrentNode = self.head #Đặt biến CurrentNode là biến chạy
            #Đặt điều kiện để next chạy đế Node kề cuối, thì lúc này next của Node kề cuối là next trỏ tới phần tử cuối
            while (CurrentNode.next!= None): 
                CurrentNode = CurrentNode.next #dịch chuyển node bằng cách trỏ tới next
            return CurrentNode.data #Trả về data của Node cuối
        
    def Print_Stack(self): #In ra Stack
        list = [] #tạo list rỗng ban đầu để đưa stack vào
        CurrentNode = self.head #đặt biến CurrentNode để làm biến chạy cho head
        if self.head is None: #Kiểm tra xem mảng có rỗng hay không
            return #Nếu có thì trả về None
        else:
            while (CurrentNode): #Điều kiện để CurrentNode chạy đến cuối
                list.append(CurrentNode.data) #chèn phần tử của Node vào trong list
                CurrentNode = CurrentNode.next #dịch chuyển node đến node tiếp theo thông qua next
            print(list) #in ra list sau khi đã chạy xong CurrentNode

Stack1 = Stack()
Stack1.Push(5)
Stack1.Push(6)
Stack1.Print_Stack()
Stack1.Print_Stack()
print(Stack1.Top() + 1)
print(Stack1.IsEmpty())
Stack1.Length_Stack()




