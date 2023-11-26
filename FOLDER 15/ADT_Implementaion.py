import numpy as np

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

# #Undirected Graph
# G = Graph(4) #khởi tạo ma trận vuông cấp 4 để trỏ tới vùng của vertices
# G.Display_AdjMat() #in ra ma trận cấp 4 vừa khởi tạo
# print("Vertices:", G.Vertex_Count()) #trỏ tới để đếm số vertex của ma trận vừa khởi tạo
# #in ra số edge của hàm vừa khởi tạo, vì chỉ mới khởi tạo vertices 
# #nên sẽ chưa có các giá trị cụ thể để trỏ tới tạo ra các cạnh
# print("Edges:", G.Edge_Count()) 
# Tạo liên kết cho một Undirected Graph
# G.Insert_Edge(0, 1) #liên kết của vertice-0 và vertice-1 
# G.Insert_Edge(0, 2) #liên kết của vertice-0 và vertice-2 
# G.Insert_Edge(1, 0) #liên kết của vertice-1 và vertice-0 
# G.Insert_Edge(1, 2) #liên kết của vertice-1 và vertice-2 
# G.Insert_Edge(2, 0) #liên kết của vertice-2 và vertice-0 
# G.Insert_Edge(2, 1) #liên kết của vertice-2 và vertice-1 
# G.Insert_Edge(2, 3) #liên kết của vertice-2 và vertice-3 G.Insert_Edge(3, 2, 6) #liên kết của vertice-3 và vertice-2 # G.Display_AdjMat() #in ra ma trận của graph vừa mới tạo liên kết
# print("Edge:",G.Edge_Count()) #trả về số cạnh của graph sau khi đã tạo liên kết
# print("Edge between 1-2:", G.Exist_Edge(1, 2)) #in ra True bởi vì có sự tồn tại edge của: vertice-1 và vertice 2
# print("Edge between 1-3:", G.Exist_Edge(1, 3)) #in ra False bởi vì không tồn tại edge của: vertice-1 và vertice 2
# G.Edges()
# G.Vertices()

#Weighted Undirected Graph
# G = Graph(4) #khởi tạo ma trận vuông cấp 4 để trỏ tới vùng của vertices
# G.Display_AdjMat()
# print("Vertices:", G.Vertex_Count()) #trỏ tới để đếm số vertex của ma trận vừa khởi tạo
# #in ra số edge của hàm vừa khởi tạo, vì chỉ mới khởi tạo vertices 
# # nên sẽ chưa có các giá trị cụ thể để trỏ tới tạo ra các cạnh
# print("Edges:", G.Edge_Count()) 
# #Tạo liên kết cho một Undirected Graph
# G.Insert_Edge(0, 1, 26) #liên kết của vertice-0 và vertice-1 có thêm weight = 26
# G.Insert_Edge(0, 2, 19) #liên kết của vertice-0 và vertice-2 có thêm weight = 19
# G.Insert_Edge(1, 0, 26) #liên kết của vertice-1 và vertice-0 có thêm weight = 26
# G.Insert_Edge(1, 2, 7) #liên kết của vertice-1 và vertice-2 có thêm weight = 7
# G.Insert_Edge(2, 0, 19) #liên kết của vertice-2 và vertice-0 có thêm weight = 19
# G.Insert_Edge(2, 1, 7) #liên kết của vertice-2 và vertice-1 có thêm weight = 7
# G.Insert_Edge(2, 3, 6) #liên kết của vertice-2 và vertice-3 có thêm weight = 6
# G.Insert_Edge(3, 2, 6) #liên kết của vertice-3 và vertice-2 có thêm weight = 6
# G.Display_AdjMat() #in ra ma trận của graph vừa mới tạo liên kết
# print("Edge:",G.Edge_Count()) #trả về số cạnh của graph sau khi đã tạo liên kết
# print("Edge between 1-2:", G.Exist_Edge(1, 2)) #in ra True bởi vì có sự tồn tại edge của: vertice-1 và vertice 2
# print("Edge between 1-3:", G.Exist_Edge(1, 3)) #in ra False bởi vì không tồn tại edge của: vertice-1 và vertice 2
# G.Edges()
# G.Vertices()

#Directed Graph
# G = Graph(4) #khởi tạo ma trận vuông cấp 4 để trỏ tới vùng của vertices
# print("Vertices:", G.Vertex_Count()) #trỏ tới để đếm số vertex của ma trận vừa khởi tạo
# #in ra số edge của hàm vừa khởi tạo, vì chỉ mới khởi tạo vertices 
# # nên sẽ chưa có các giá trị cụ thể để trỏ tới tạo ra các cạnh
# print("Edges:", G.Edge_Count()) 
# #Tạo liên kết cho một Undirected Graph
# G.Insert_Edge(0, 1) #liên kết của vertice-0 và vertice-1 
# G.Insert_Edge(0, 2) #liên kết của vertice-0 và vertice-2 
# G.Insert_Edge(1, 2) #liên kết của vertice-1 và vertice-2 
# G.Insert_Edge(2, 3) #liên kết của vertice-2 và vertice-3 print("Edge:",G.Edge_Count()) 
# #trả về số cạnh của graph sau khi đã tạo liên kết
# print("Edge between 1-2:", G.Exist_Edge(1, 2)) #in ra True bởi vì có sự tồn tại edge của: vertice-1 và vertice 2
# print("Edge between 1-3:", G.Exist_Edge(1, 3)) #in ra False bởi vì không tồn tại edge của: vertice-1 và vertice 3
# G.Edges()
# G.Vertices()
# G.Display_AdjMat()

#Weight Directed Graph
# G = Graph(4) #khởi tạo ma trận vuông cấp 4 để trỏ tới vùng của vertices
# print("Vertices:", G.Vertex_Count()) #trỏ tới để đếm số vertex của ma trận vừa khởi tạo
# #in ra số edge của hàm vừa khởi tạo, vì chỉ mới khởi tạo vertices 
# # nên sẽ chưa có các giá trị cụ thể để trỏ tới tạo ra các cạnh
# print("Edges:", G.Edge_Count()) 
# #Tạo liên kết cho một Undirected Graph
# G.Insert_Edge(0, 1, 16) #liên kết của vertice-0 và vertice-1 có thêm weight = 16
# G.Insert_Edge(0, 2, 15) #liên kết của vertice-0 và vertice-2 có thêm weight = 15
# G.Insert_Edge(1, 2, 9) #liên kết của vertice-1 và vertice-2 có thêm weight = 9
# G.Insert_Edge(2, 3, 6) #liên kết của vertice-2 và vertice-3 có thêm weight = 6
# print("Edge:",G.Edge_Count()) #trả về số cạnh của graph sau khi đã tạo liên kết
# print("Edge between 1-2:", G.Exist_Edge(1, 2)) #in ra True bởi vì có sự tồn tại edge của: vertice-1 và vertice 2
# print("Edge between 1-3:", G.Exist_Edge(1, 3)) #in ra False bởi vì không tồn tại edge của: vertice-1 và vertice 3
# G.Edges()
# G.Vertices()
# G.Display_AdjMat()

















