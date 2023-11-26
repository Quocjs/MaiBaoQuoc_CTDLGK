def quick_sort(arr, left, right): #hàm quick_sort để lưu ý array thõa mãn để tiếp tục làm việc 
    if left < right:
        pivot = sort(arr, left, right) #đặt sort thõa mãn theo thứ tự accesding của array
        quick_sort(arr, left, pivot-1) #sort cho array bên trái
        quick_sort(arr, pivot+1, right) #sort cho array bên phải

def sort(arr, left, right):
    i = left #đặt phần tử bên trái có biến chạy là i
    j = right-1 #đặt phần tử bên phải có biến chạy là j nhưng vì nhỏ hơn pivot nên chạy đến right -1
    pivot = arr[right] #phần tử cuối cùng của array là pivot

    while i < j: #đặt điều kiện để chạy i và j liên tục, thể hiện tính logic của vị trí i và j
        while i < right and arr[i] < pivot: #điều kiện nếu phần tử i thõa mãn thì liên tục trượt i
            i+=1 #tăng i lên để thoát khỏi vòng lặp trượt - có thể gọi là tiến lên về bên phải
        while j > left and arr[i] >= pivot: #điều kiện nếu phần tử i thõa mãn thì liên tục trượt j
            j-=1 #giảm j lên để thoát khỏi vòng lặp trượt - có thể gọi là lùi về bên trái
        if i < j: #điều kiện trên vẫn đúng
            arr[i], arr[j] = arr[j], arr[i] #swap khi lúc này không thõa mãn điều kiện của while nữa
    if arr[i] > pivot: #điều kiện khi j chạy khỏi i hay lúc này j < i nghĩa là biến left ở phía bên phải
        arr[i], arr[right] = arr[right], arr[i] #swap left và pivot để tạo ra 2 array con và tiếp tục đệ quy để sort
    return i #trả về i để tiếp tục dùng sorted liên tục, đối số cho quick_sort bên trên

A = [22, 17, 88, 63, 57, 77, 34, 14]
print(A)
quick_sort(A, 0, len(A)-1) #bởi vì j chỉ chạy đến phần từ liền kề trước của array nên là len(A) - 1
print(A)





