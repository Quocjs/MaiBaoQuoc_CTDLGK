def Bucket_Sort(A):
    n = len(A) #tạo độ dài của vòng lặp đúng bằng độ dàu của mảng A
    MaxElement = max(A) #tìm phần tử lớn nhất trong mảng A
    l = [] #tạo bucket trống
    Buckets = [l]*10 #tạo 10 bucket trống
    
    for i in range(n):
        #Vị trí của bucket được tính bằng cách lấy phần nguyên của phép chia n * A[i] cho MaxElement + 1.
        j = int(n*A[i] / (MaxElement + 1))
        if len(Buckets[j]) == 0:
            #Chèn từng phần tử A[i] vào bucket Buckets[j], trong đó j là vị trí của bucket cần chèn. 
            Buckets[j] = [A[i]]
        else:
            Buckets[j].append(A[i])
    
    # Sử dụng thuật toán sắp xếp chèn để sắp xếp từng bucket.
    for i in range(10):
        Insertion_Sort(Buckets[i])

    #Trả về mảng A đã được sắp xếp theo thứ tự tăng dần.
    k = 0
    for i in range(10):
        for j in range(len(Buckets[i])):
            A[k] = Buckets[i].pop(0)
            k = k + 1

#Hàm sử dụng thuật toán Insertion_Sort
def Insertion_Sort(A):
    n = len(A)
    for i in range(1, n):
        cvalue = A[i]
        position = i
        while (position > 0 and A[position-1] > cvalue):
            A[position] = A[position-1]
            position = position -1
        A[position] = cvalue



A = [13, 2, 6, 18, 5, 99, 0, 1]
print("Mảng ban đầu:", A)
Bucket_Sort(A) 
print("Mảng sau khi được sorted:", A)










