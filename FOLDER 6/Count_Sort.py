A = [10, 7, 12, 4, 9, 13]

Max_index = max(A) #tìm phần tử lớn nhất trong mảng
Count = [0]*(Max_index+1) #tạo ra một mảng count có kích thước bằng phần tử lớn nhất trong mảng

for num in A:
    Count[num] += 1 #đếm tần số suất hiện của phần tử trong mảng A

for i in range(1, Max_index + 1): #tạo sum của đếm tần số
    Count[i] += Count[i - 1]

output_array = [0] * len(A) #tạo một mảng in ra có kích thước bằng mảng ban đầu

for i in range(0, len(A), 1):
    output_array[Count[A[i]]-1] = A[i] #in ra giá trị của mảng mới tại vị trí của sum_count bẳng với giá trị của mảng ban đầu
    Count[A[i]]-=1 #sum_count giảm đi 1 lần để đếm các tần số bị lặp lại


print(output_array)




