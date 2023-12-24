A=[]
while True:
    gia_tri=int(input("nhập giá trị:\n"))
    A.append(gia_tri)
    tiep_tuc=input("thêm giá trị 1:đồng ý, 0:thôi\n")
    if tiep_tuc!='1':
        break
print("list:", A)
tong=sum(A)
print("tổng các phần tử trong list là:", tong)
so_can_tim=int(input("nhập số cần tìm:"))
so_lan_xuat_hien= A.count(so_can_tim)
print(f"số {so_can_tim} xuất hiện {so_lan_xuat_hien} lần")
if so_can_tim>= max(A):
    print(f"{so_can_tim} không lớn hơn tất cả các số trong list") 
else:
    lon_hon = [num for num in A if num > so_can_tim]
print(f"Các số lớn hơn {so_can_tim} trong list: {lon_hon}")

   