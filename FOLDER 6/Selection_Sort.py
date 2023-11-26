def Selection_Sort(arr):
    for i in range(len(arr)): #thực hiện quét các phần tử của i để so sánh
        index_mm = i #gán phần tử cần đi quét ban đầu bằng i
        for j in range(i+1, len(arr)): #quét các phần tử còn lại so với phần tử ban đầu của mảng
            if arr[j] < arr[index_mm]: #kiểm tra để swap 2 phần tử
                index_mm = j #swap vị trí phần tử
        arr[i], arr[index_mm] = arr[index_mm], arr[i] #swap 2 phần tử sau cùng, sau khi đã swap hoàn tất
    return arr #trả lại arr để sử dụng
A = [64, 25, 12, 22, 11]
print("Chưa Sorted: ",A)
print("Đã được Sort:", Selection_Sort(A)) #in ra hàm A đã được sử dụng hàm Selection_sort





