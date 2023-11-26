def merge_sort(arr):
    if len(arr)>1: #điều kiện để chia đến cuối, tức là phần tử sau cùng chia là phải tối thiểu là 1
        left_array = arr[:len(arr)//2] #chia thành array bên trái từ vị trí ở middle của chuỗi
        right_array = arr[len(arr)//2:] #chia thành array bên phải tử vị trí của middle của chuỗi
    
        merge_sort(left_array) #tạo đệ quy cho chạy bên trái liên tục đến khi phần tử chia tối thiểu là 1
        merge_sort(right_array) #tạo đệ quy cho chạy bên phải liên tục đến khi phần tử chia tối thiểu là 1

        i = 0 #tạo biến chạy cho mảng bên trái
        j = 0 #tạo biến chạy cho mảng bên phải
        k = 0 #tạo biến chạy cho mảng merge (mảng xác nhập hai mảng trên nếu thõa điều kiện)
        
        while i < len(left_array) and j < len(right_array): #kiểm tra điều kiện lấy của hai mảng
            if (left_array[i] < right_array[j]): #nếu bên trái nhỏ hơn bên phải
                arr[k] = left_array[i] #thì array xuất sẽ lấy phần tử bên trái
                i = i+1 #tăng biến đếm để xét phần tử tiếp theo của mảng bên trái
            else:
                arr[k] = right_array[j] #nếu không thõa mãn bên trái thì làm với mảng bê phải
                j = j+1 #tăng biến đếm để xét phần tử tiếp theo của mảng bên phải
            k = k+1 #tăng phần tử xuất ra lên để đếm hết phần tử của mảng merge (mảng nhập)

        while (i < len(left_array)): #kiểm tra phần tử còn lại bên trái của mảng nếu thõa mãn thì nhập lại vào mảng xuất
            arr[k] = left_array[i] 
            i = i+1
            k = k+1

        while (j < len(right_array)): #kiểm tra phần tử còn lại bên phải của mảng nếu thõa mãn thì nhập lại vào mảng xuất
            arr[k] = right_array[j]
            j = j+1
            k = k+1
        
A = [4, 10, 8, 7, 45, 99, 1, 2, 7]
print(A)
merge_sort(A)
print(A)


