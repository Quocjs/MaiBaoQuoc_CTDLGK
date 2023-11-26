import numpy as np
from Ques_Array import Queues_Array

class Graph:
    #Khởi tạo hàm tạo Graph, đơn vị đơn giản nhất của graph là vertices
    def __init__(self, vertices): 
        # Lấy giá trị vertices (đỉnh)
        self.vertices = vertices
        # Khởi tạo không gian ma trận cấp n*n với n là chỉ số vertices được truyền vào
        self.adjMat = np.zeros((vertices, vertices)) 
    
    #Hàm khởi tạo Edge(cạnh)
    def Insert_Edge(self, u, v, x = 1): 
        self.adjMat[u][v] = x #tạo 1 cạnh từ u đến v thì ma trận đánh dấu là 1

    #Hàm xóa Edge(cạnh)
    def Remove_Edge(self, u, v):
        self.adjMat[u][v] #xóa đi liên kết giữa u và v thì ma trận sẽ đánh dấu là 0
    
    #Hàm thoát khỏi cạnh
    def Exist_Edge(self, u, v):
        return self.adjMat[u][v] != 0 #trả về chính nó(edge giữa u và v) nếu không bị xóa
    
    #Hàm in ra số vertex
    def Vertex_Count(self): 
        #trả về số vertices của graph số này đúng bằng với chỉ số đưa vào hàm ma trận khởi tạo
        return self.vertices 
    
    #Hàm đếm số cạnh trong ma trận
    def Edge_Count(self):
        count = 0 #đặt ban đầu số đếm là 0
        for i in range(self.vertices): #vòng lặp để quét cạnh trên
            for j  in range(self.vertices): #vòng lặp để quét cạnh bên 
                if self.adjMat[i][j] != 0: #nếu tồn tại chỉ số tại i, j khác 0 cụ thể là 1
                    count = count + 1 #thì tăng đếm lên 1
        return count #trả về giá trị đếm được
    
    def Vertices(self): #in ra các Vertices tồn tại bên trong Graph
        for i in range(self.vertices):
            print(i, end='.')
        print()
    
    #In ra các Edges tồn tại bên trong graph
    def Edges(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjMat[i][j] != 0: #nếu tồn tại Edge, cụ thể là 1, !=0 chỉ mang tính tượng trưng
                    print(i, '--', j) #in ra liên kết giữa nguồn và đích
    
    #Hàm đếm số edge chạy từ bên trong ra khỏi v
    def Outdegree(self, v):
        count = 0 #Khởi tạo biến đếm ban đầu là 0
        for j in range(self.vertices): #vòng lặp chạy cho vòng trên
            if self.adjMat[v][j] != 0: #chạy trên vòng lặp được đặt ở đây là gốc là v
                count = count + 1 #tăng biến đếm lên 1 nếu tồn tại edge bên trong vòng lặp 
        return count #trả về số lượng edge đã đếm được 
    
    #Hàm đếm số edge chạy từ bên ngoài vào trong v
    def Indegree(self, v):
        count = 0 #Khởi tạo biến đếm ban đầu là 0
        for i in range(self.vertices): #vòng lặp chạy cho cạnh bên
            if self.adjMat[i][v] != 0: #chạy trên vòng lặp được đặt ở đây đích là v
                count = count + 1 #tăng biến đếm lên 1 nếu tồn tại edge bên trong vòng lặp 
        return count #trả về số lượng edge đã đếm được 
    
    #Hàm in ra ma trận
    def Display_AdjMat(self): 
        print(self.adjMat) #in ra ma trận

    #Hàm tìm đường đi quét hết tất cả các vertices bằng thuật toán breadth first search
    def Breadth_First_Search(self, s):
        i = s #đặt biến để thực thi từ gốc s của Breadth
        q = Queues_Array() #đặt q là object của Queues
        visited = [0]*self.vertices #đặt số lần gặp Vertices(đỉnh) của Graph đúng bằng số Vertices(đỉnh)
        print(i, end='') #in ra các lần gặp đỉnh lần lượt và quét hết các phần tử xung quanh Vertices
        visited[i] = 1 #quy định đã gặp Vertices nào đó thì nó là 1
        q.Enqueue(i) #gán gốc i vào danh sách của queue
        #kiểm tra ban đầu q có rỗng hay không, nghĩa là đi tới 1 vertice nào đó mà không có edge trỏ tới vertices nào nữa
        while not q.IsEmpty(): 
            i = q.Dequeue() #đưa trở lại vertice vào thực hiện tiếp tục ghé thăm từ vertices
            for j in range(self.vertices): #chỉ số đích của ma trận vertices
                #điều kiện để biết là có liên kết của u và v đồng thời là chưa được visited 
                if self.adjMat[i][j] == 1 and visited[j] == 0: 
                    print(j, end= '') #in ra đích cho đẹp
                    visited[j] = 1 #quy định lại đích là 1 nghĩa là đã gặp
                    #Đưa đích(vertices) vào queue và thực hiện tiếp tục cho đến khi không còn đích nào nữa, 
                    # nghĩa là không còn j nào trong ma trận mà thõa mãn visited[j] == 0
                    q.Enqueue(j) 

G = Graph(7)
G.Insert_Edge(0, 1)
G.Insert_Edge(0, 5)
G.Insert_Edge(0, 6)
G.Insert_Edge(1, 0)
G.Insert_Edge(1, 2)
G.Insert_Edge(1, 5)
G.Insert_Edge(1, 6)
G.Insert_Edge(2, 3)
G.Insert_Edge(2, 4)
G.Insert_Edge(2, 6)
G.Insert_Edge(3, 4)
G.Insert_Edge(4, 2)
G.Insert_Edge(4, 5)
G.Insert_Edge(5, 2)
G.Insert_Edge(5, 3)
G.Insert_Edge(6, 3)
print("BFS")
G.Breadth_First_Search(0)

