def Insertion_Sort(A):
    for i in range(1, len(A)): #tạo biến chạy index của biến temp
        temp = A[i] #gán biến temp cho biến chạy
        j = i-1 #gán biến quét từng phần tử của mảng
        while (j >=0 and A[j] >= temp): #kiểm tra phần tử mảng với điều kiện của temp
            #swap thành phần của mảng A thõa mãn
            A[j+1]=A[j] 
            A[j] = temp
            j-=1
        A[j+1]=temp #nếu không swap, hoặc đã swap xong thì gắn lại biến chạy cho temp
    return A
A = [13, 2, 6, 18, 5, 99, 0, 1]
print(A)
print(Insertion_Sort(A)) #in ra mảng mới sau khi đã sort










