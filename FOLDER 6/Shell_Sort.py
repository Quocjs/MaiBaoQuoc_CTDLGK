def shell_sort(arr):
    gap = len(arr)//2  #tính số cách nhau của phần tử cần swap
    while (gap > 0): #tạo điều kiện gap tối thiểu là 1
        j = gap #đặt biến chạy cho gap
        while(j < len(arr)): #điều kiện tồn tại gap
            i = j - gap #phần tử của mảng để dịch theo gap
            while (i >= 0): #điều kiện để quét hết array, mà không lặp lại theo chiều ngược lại 
                if arr[i+gap] > arr[i]: #nếu phần tử cách phần tử duyệt 1 khoảng gap đã được sorted
                    break #dừng không cho sorted
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap] #còn nếu không thì swap phần tử được duyệt và phần tử cách khoảng gap
                i = i-gap #đặt lại biến chạy cho phần tử chạy liên tục
            j+=1 #tăng j để có thể tiếp tục chạy biến đếm của gap ở vị trí phần tử tiếp theo 
        gap = gap//2 #tiếp tục giảm gap để chạy cho những phần tiếp theo

A = [33, 22, 55, 7, 8]
print(A)
shell_sort(A)
print(A)








