def radixSort(arr):

    # Tìm số lớn nhất trong mảng arr để xác định số lượng chữ số
    max1 = max(arr)
    # Biến exp sẽ lưu trữ cơ số của hệ đếm
    exp = 1
    # Duyệt qua từng chữ số
    while max1 // exp >= 1:
        # Sử dụng thuật toán counting sort để sắp xếp các phần tử trong mảng arr theo chữ số hiện tại
        countingSort(arr, exp)
        # Tăng giá trị của exp lên 1
        exp *= 10
# Hàm counting sort để sắp xếp các phần tử trong mảng theo một chữ số
def countingSort(arr, exp1):
    # Tìm độ dài của mảng arr
    n = len(arr)
    # Khởi tạo mảng output để lưu trữ kết quả sau khi sắp xếp
    output = [0] * (n)
    # Khởi tạo mảng count để lưu trữ tần suất xuất hiện của các chữ số trong mảng arr
    count = [0] * (10)
    # Duyệt qua các phần tử trong mảng arr và đếm số lần xuất hiện của từng chữ số
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    # Cập nhật mảng count để lưu trữ vị trí thực tế của từng chữ số trong mảng output
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Xây dựng mảng output bằng cách sắp xếp các phần tử trong mảng arr theo vị trí thực tế của chúng
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    # Sao chép mảng output vào mảng arr để mảng arr chứa các số đã được sắp xếp
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(arr)
# Gọi hàm radixSort để sắp xếp mảng arr
radixSort(arr)
print(arr)

