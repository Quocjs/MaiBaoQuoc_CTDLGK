#Linear Algorithm
#ý tưởng để triển khai bài toán này là duyệt phần tử từ đầu[index = 0] đến cuối[index = len(object)-1], sau đó
#xét element có giá trị trùng với key.
def Linear_Search(A, key):
    i = 0 #gán phần tử duyệt = 1
    while (i <= len(A)-1): #xét điều kiện để phần tử duyệt từ đầu đến cuối.
        if key == A[i]: #kiểm tra phần tử có trùng với index hay không.
            return i #trả về index của phần tử.
        i+=1 #tăng phần tử đệm để xét tiếp trong vòng lặp while.
    return -1 #trả về -1 khi điều kiện chạy vòng lặp ở trên không còn đúng nữa.


A = [1, 4, 6, 7, 13]
a = Linear_Search(A, 13)
# print("Vị trí(index) của phần tử cần tìm là:",a)


#Binary Algorithm
def Binary_Search(A, key):
    l =  0 #gán vị trí cho phần tử đầu tiên
    r = len(A)-1 #gán vị trí cho phần tử cuối cùng 
    while(l <= r): #kiểm tra điều kiện để 2 vị trí đầu và cuối không bị sai về mặt logic
        mid = (l+r)//2 #lấy vị trí đệm. floor nên sẽ ưu tiên phần tử bên trái(tròn về nguyên)
        if key == A[mid]: #nếu vị trí của key trùng với vị trí chính giữa
            return mid #trả về vị trí của phần tử chính giữa mảng
        elif key > A[mid]: #kiểm tra nếu key lớn hơn phần tử chính giữa của mảng
            l = mid+1 #dịch khoảng đầu duyệt lên vị trí của vị trí phần tử giữa thêm 1. 
            #(nghĩa là lúc này khoảng để kiểm tra từ vị trí chính giữa + 1 đến r)
        elif key < A[mid]: #kiểm tra nếu key nhỏ hơn phần tử chính giữa của mảng
            r = mid-1 #dịch khoảng cuối duyệt xuống vị trí của vị trí phần tử giữa trừ 1. 
            #(nghĩa là lúc này khoảng để kiểm tra từ vị trí l đến chính giữa -1)
    return -1 #trả về -1 khi điều kiện while không còn đúng nữa


A = [1, 4, 6, 7, 13]
found = Binary_Search(A, 13)
#print("Vị trí(index) của phần tử cần tìm là:",found)





#Binary Recursion Alrorithm 
def Binary_Recustion(A, key, L, H):
    if (L > H): #xét điều kiện để vị trí khi vị trí đầu lớn vị trí cuối --> Không tồn tại Array nào
        return -1 #trả về -1
    else:
        mid = (L+H )//2 #tính vị trí của đệm.
        if key == A[mid]: #kiểm tra xem key có bằng phần tử giữa của mảng hay không
            return mid #trả về vị trí giữa nếu key trùng với phần tử giữa
        elif key < A[mid]: #kiểm tra nếu key nhỏ hơn phần tử giữa
            return Binary_Recustion(A, key, L, mid-1) #trả ngược lại về hàm nhưng xét trên khoảng từ L đến mid-1
        elif key > A[mid]: #kiểm tra nếu key lớn hơn phần tử giữa
            return Binary_Recustion(A, key, mid+1, H) #trả ngược lại hàm nhưng xét trên khoảng từ mid+1 đến H

A = [1, 4, 6, 7, 13]        
a = Binary_Recustion(A, 13, 0, len(A)-1)
print("Vị trí(index) của phần tử là:",a)

        



