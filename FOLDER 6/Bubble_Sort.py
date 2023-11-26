def Bubble_Sort(A):
    for i in range(len(A)): #tạo index lần chạy cho thuật toán, ở bài toán tổng quát thì phải chạy n lần
        for j in range(len(A)-1): #tạo vòng lặp cho biến chạy hai phần tử liền kề
            if A[j] > A[j+1]: #điều kiện để swap
                A[j], A[j+1] = A[j+1], A[j] #swap hai phần tử liền kề với nhau
    return A #trả về lại mảng sau khi đã quét xong

Array = [10, 7, 3, 13, 2, 4]
print(Array)
print(Bubble_Sort(Array)) #in ra mảng mới sau khi đã được sorted

