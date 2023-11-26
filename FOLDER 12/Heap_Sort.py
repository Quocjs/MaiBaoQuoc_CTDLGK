from Heap import Heap

def Heapsort(A):

    # Khởi tạo một heap trống.
    H = Heap()
    # Tính độ dài của mảng.
    n = len(A)
    # Chèn từng phần tử của mảng vào heap.
    for i in range(n):
        # H.Insert(A[i]) chèn phần tử A[i]vào heap.
        H.Insert(A[i])
    # Bắt đầu từ phần tử cuối cùng của mảng, chèn từng phần tử vào mảng.
    k = n - 1
    for i in range(H.csize):
        # A[k] lưu trữ phần tử lớn nhất của heap.
        A[k] = H.DeleteMax()
        # k giảm xuống 1.
        k = k - 1

A = [63, 250, 835, 947, 651, 28]
# In mảng ban đầu.
print("Mảng ban đầu:", A)
# Sắp xếp mảng.
Heapsort(A)
# In mảng đã được sắp xếp.
print("Mảng đã được sorted:", A)

