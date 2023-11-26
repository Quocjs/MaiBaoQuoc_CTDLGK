class HashLinearProbe:

    # Định nghĩa một lớp có tên `HashLinearProbe`.

    def __init__(self):

        # Khởi tạo đối tượng `HashLinearProbe`.
        # Đặt kích thước bảng băm thành 10.
        self.hashtable_size = 10

        # Tạo một bảng băm trống.
        self.hashtable = [0] * self.hashtable_size

    # Tính hàm băm cho một khóa cho trước.
    # Sử dụng toán tử modulo (`%`) để phân phối các khóa đồng đều trên bảng băm.
    def hashcode(self, key):
        return key % self.hashtable_size

    # Tìm một ô trống cho một phần tử cho trước.
    # Bắt đầu tại hash code của phần tử và thăm dò các ô tiếp theo cho đến khi tìm thấy một ô trống.
    def lprobe(self, element):
        i = self.hashcode(element)
        j = 0
        while self.hashtable[(i + j) % self.hashtable_size] != 0:
            j = j + 1
        return (i + j) % self.hashtable_size

    # Chèn một phần tử vào bảng băm.
    # Đầu tiên tính hàm băm cho phần tử và kiểm tra xem ô tương ứng có trống hay không.
    # Nếu ô trống, chèn phần tử.
    # Ngược lại, sử dụng linear probing để tìm một ô trống và chèn phần tử vào đó.
    def insert(self, element):
        i = self.hashcode(element)
        if self.hashtable[i] == 0:
            self.hashtable[i] = element
        else:
            i = self.lprobe(element)
            self.hashtable[i] = element

    # Tìm kiếm một phần tử trong bảng băm.
    # Đầu tiên tính hàm băm cho khóa và thăm dò các ô tiếp theo bằng linear probing.
    # Nếu tìm thấy khóa, trả về `True`.
    # Ngược lại, trả về `False`.
    def search(self, key):
        i = self.hashcode(key)
        j = 0
        while self.hashtable[(i + j) % self.hashtable_size] != key:
            if self.hashtable[(i + j) % self.hashtable_size] == 0:
                return False
            j = j + 1
        return True

    # Hiển thị nội dung của bảng băm.
    # Chỉ đơn giản là in bảng băm dưới dạng một danh sách.
    def display(self):
        print(self.hashtable)

H = HashLinearProbe()
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)
H.insert(34)
H.insert(86)
H.insert(28)
H.display()
print("Result", H.search(54))


