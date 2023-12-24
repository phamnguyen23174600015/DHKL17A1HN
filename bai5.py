A=[]
while True:
    gia_tri=int(input("nhập giá trị:\n"))
    A.append(gia_tri)
    tiep_tuc=input("thêm giá trị 1:đồng ý, 0:thôi\n")
    if tiep_tuc!='1':
        break

so_am = [num for num in A if num < 0 ]
so_duong = [num for num in A if num > 0 ]
print("số âm trong list là: ", so_am)
#trung bình cộng
tong_am = sum(so_am)
tong_duong = sum(so_duong)
pt_so_am = len(so_am)
pt_so_duong = len(so_duong)
trung_binh_am = tong_am / pt_so_am
trung_binh_duong = tong_duong / pt_so_duong
print("trung bình cộng các phần tử âm là: ", trung_binh_am )
print("trung bình cộng các phần tử dương là: ", trung_binh_duong )
# max min 
max = max(A)
min = min(A)
print("Max A: ", max)
print("Min A: ", min)
#
tang_dan = sorted(A)
print("danh sách tăng dần là:", tang_dan)




