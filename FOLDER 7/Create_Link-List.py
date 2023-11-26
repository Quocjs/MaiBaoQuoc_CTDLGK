class Node:
    def __init__(self, data): #tạo thành phần cơ bản của đơn vị Node
        self.data = data #đặt giá trị đầu là data truyền vào
        self.next = None #ban đầu next là None
    
class LinKed_List:
    def __init__(self):
        self.head = None #thành phần cơ bản cấu thành Linked List
    #Hàm Insert:
    def Insert_Begin(self, data): #Hàm thêm giá trị vào đầu list
        NewNode = Node(data) #giá trị cần thêm vào đầu list
        if self.head is None: #trường hợp nếu ban đầu list là rỗng
            self.head = NewNode #cho head mặc định là giá trị truyền vào
            return #trả về None cho trường chỉ có 1 Node 
        #trường hợp nếu ban đầu không rỗng
        NewNode.next = self.head #next của data muốn truyền vào chính là head
        self.head = NewNode #lúc này head chưa có giá trị nên phải truyền head bằng chính giá trị của data truyền vào
    
    def Insert_End(self, data): #hàm thêm giá trị vào cuối linked list
        NewNode = Node(data) #giá trị cần thêm vào đầu list
        if self.head is None: #trường hợp nếu ban đầu list là rỗng
            self.head = NewNode #cho head mặc định là giá trị truyền vào
            return #trả về None cho trường chỉ có 1 Node 
        
        CurrentNode = self.head #đặt head là biến chạy
        while (CurrentNode.next): #dịch chuyển cho đến khi next chạy đến trước None 1 Node
            CurrentNode = CurrentNode.next #dịch chuyển next sang node khác
        CurrentNode.next = NewNode #đưa next của phần tử cuối gán vào giá trị muốn thêm

    def Insert_Index(self, data, index): #hàm thêm giá trị vào vị trí index của linked list
        NewNode = Node(data) #giá trị node cần thêm vào
        position = 0 #biến chạy
        if position == index: #trường hợp index trùng với giá trị đầu
            self.Insert_Begin(data) 
        else:
            CurrentNode = self.head #đặt biến để lấy head làm biến chạy
            while (CurrentNode != None and position + 1 != index): #vòng lặp dùng để dịch chuyển next
                position = position + 1 #tăng position nếu index không thõa mãn
                CurrentNode = CurrentNode.next #dịch chuyển next
            NewNode.next = CurrentNode.next #chuyển next mới bằng với next cũ
            CurrentNode.next = NewNode #chuyển next cũ bằng giá trị mới

    #Hàm Delete:
    def Delete_Begin(self): #Hàm delete node đầu tiên
        if self.head is None: #kiểm tra mảng ban đầu có rỗng hay không
            return #trả về None nếu ban đầu mảng rỗng
        self.head = self.head.next #chuyển đổi head thành next của head, thì head cũ sẽ bị xóa

    def Delete_End(self): #Hàm delete Node cuối cùng
        if self.head is None: #kiểm tra mảng ban đầu có rỗng hay không
            return #trả về None nếu ban đầu mảng rỗng
        CurrentNode = self.head #đặt head là biến chạy
        while(CurrentNode.next.next != None): #kiểm tra điều kiện để tồn tại node cuối mà không cần kiểm tra next cuối
            CurrentNode = CurrentNode.next #dịch chuyển next
        CurrentNode.next = None #cho node kề cuối có next là none để loại bỏ node cuối
    
    def Delete_Index(self, index):
        if self.head is None: #kiểm tra mảng ban đầu có rỗng hay không
            return #trả về None nếu ban đầu mảng rỗng
        position = 0 # đặt biến chạy
        if position == index:
            self.Delete_Begin()
        CurrentNode = self.head #đặt biến head là biến chạy
        while(CurrentNode != None and position + 1 != index):
                position = position + 1
                CurrentNode = CurrentNode.next
        CurrentNode.next = CurrentNode.next.next #xóa bỏ đi node ở vị trí index
    
    def Delete_Node(self, val):
        if self.head is None: #kiểm tra mảng ban đầu có rỗng hay không
            return #trả về None nếu ban đầu mảng rỗng
        
        CurrentNode = self.head #đặt head là biến chạy
        while (CurrentNode != None and CurrentNode.next.data != val): #điều kiện để dừng đúng node cần chuyển
            CurrentNode = CurrentNode.next #chuyển next
        CurrentNode.next = CurrentNode.next.next #xóa bỏ đi node ở vị trí index

    #Hàm Update:

    def Update_Index(self, index, val): #update giá trị bởi index
        if self.head is None: #kiểm tra mảng ban đầu có rỗng hay không
            return #trả về None nếu ban đầu mảng rỗng
        position = 0 #đặt biến chạy
        CurrentNode = self.head #đặt head là biến chạy
        while (CurrentNode != None and position != index): #điều kiện để postion trỏ đúng vào index cần tìm 
            position = position + 1 #tăng position để tiếp tục tìm đúng với index
            CurrentNode = CurrentNode.next #dịch chuyển next
        CurrentNode.data = val #gán giá trị cần đổi vào node chạy 

    def Size_LL(self): #hàm lấy độ dài của Linked List
        count = 0 #biến đếm
        CurrentNode = self.head #lấy head làm biến chạy
        while(CurrentNode): #điều kiện để next chạy đến cuối, trước khi gặp none
            count = count + 1 #tăng biến đếm khi next chạy đến 1 node mới 
            CurrentNode = CurrentNode.next #dịch chuyển next
        print(count) #in ra độ dài của linked List
        
    def Print_LL(self): #hàm in giá trị của linked list
        Current_Node = self.head #đặt biến chạy là head
        list = [] #tạo mảng rỗng để chứa data
        while (Current_Node): #duyệt hết list cho đến khi gặp None
            list.append(Current_Node.data) #truyền data vào mảng list
            Current_Node = Current_Node.next #di chuyển next đến next khác
        print(list) #in ra mảng

    def Search_Node(self, val):
        if self.head is None: #kiểm tra list có rỗng hay không
            return 
        index = 0 #gán giá trị cho index
        CurrentNode = self.head #đặt head là biến chạy
        while(CurrentNode != None): #điều kiện để CurrentNode có thể duyệt từ đầu đến cuối
            if (CurrentNode.data == val): #nếu data của Node bằng val thì thực hiện return 
                return f"Giá trị {val} ở vị trí: {index + 1}" #trả về vị trí của gia tri can tim
            CurrentNode = CurrentNode.next #dịch chuyển next
            index = index + 1 #tăng biến đếm index lên 1
        return "Không tồn tại giá trị nào như thế" #trả về return nếu không tồn tại val trong linked list

Link1 = LinKed_List()

Link1.Insert_Begin(9)
Link1.Insert_Begin(8)
Link1.Insert_Begin(7)
Link1.Insert_End(10)
Link1.Insert_End(11)
Link1.Insert_Begin(6)

Link1.Print_LL()
Link1.Insert_Index(5, 2)
Link1.Print_LL()
Link1.Size_LL()
Link1.Delete_Begin()
Link1.Print_LL()

Link1.Delete_End()
Link1.Print_LL()

Link1.Delete_Index(3)
Link1.Print_LL()

Link1.Delete_Node(8)
Link1.Print_LL()

Link1.Print_LL()

print(Link1.Search_Node(10))









