#1
def bai_1():
    a = [1, 2, 3]
    b = [1, [2, 3]]
    c = []
    d = [1, 2, 3][1:]
    len_a = len(a)
    len_b = len(b)
    len_c = len(c)
    len_d = len(d)
    print("Length of a:", len_a)
    print("Length of b:", len_b)
    print("Length of c:", len_c)
    print("Length of d:", len_d)
#3
def bai_3 (x, con_thu_can_tim):
    print(f"số lượng các con thú là:", {len(x)})
    if con_thu_can_tim in x:
        print(f"con {con_thu_can_tim} có trong danh sách trên")
    else:
        print(f"con {con_thu_can_tim} không có trong danh sách")
#4
def bai_4():
    while True:
        A =[]
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

#2
def bai_2(teams):
    doi_te_nhat = teams[2]
    badcap = doi_te_nhat[1]
    
    return badcap
#5
def bai_5():
   
    while True:
        A = []
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

#6
def bai_6():
    chieu_cao_inch = list(map(float,input("nhập chiều cao ").split(',')))
    chieu_cao_met = [num * 0.0254 for num in chieu_cao_inch]
    print("chiều cao theon đơn vị inch là: ", chieu_cao_inch)
    print("chiều cao theon đơn vị mét là: ", chieu_cao_met)

    print("3 chiều cao đầu tiên:", chieu_cao_met[:3])
    print("3 chiều cao cuối cùng:", chieu_cao_met[-3:])
    C = sum(chieu_cao_met)
    D = len(chieu_cao_met)
    trung_binh = C / D
    print("chiêu cao trung bình theo đơn vị mét là:", trung_binh)
    print("người cao nhất cao:", max(chieu_cao_met))
    print("người thấp nhất cao:", min(chieu_cao_met))
    chieu_cao_tang_dan = sorted(chieu_cao_met)
    chieu_cao_giam_dan = sorted(chieu_cao_met, reverse=True)
    print("chiêu cao tăng dần là:", chieu_cao_tang_dan)
    print("chiêu cao giẩm dần là:", chieu_cao_giam_dan)
    
#7
def bai_7(thresh):
    A=[]
    while True:
        gia_tri=input("nhập giá trị:\n")
        A.append(gia_tri)
        tiep_tuc=input("thêm giá trị 1:đồng ý, 0:thôi\n")
        if tiep_tuc!='1':
            break
    ket_qua = [ i > thresh for i in A ]
    print("kết quả: ", ket_qua)   

#8
def bai_8(A):
 so_may_man = [num for num in A if int(num) % 7 == 0]
 print("số may mắn là:", so_may_man)

#9
def bai_9(arrivals, name):
    khach = arrivals.index(name)  # tìm vị trí khách trong dsach
    khach_den_truoc = khach
    khach_den_tre = khach_den_truoc > len(arrivals) / 2
    return khach_den_tre
#10
def bai_10(menu):
    menu12 = tuple(menu) 
    for i in range(len(menu12)-1):
        if menu12[i] == menu12[i+1]:
            return True
    return False
 #11
def bai_11():
    A = input("nhập các phần tử:").split(' ')
    tuple1 = tuple(A)
    print(tuple)
    index_duong = int(input("nhập số từ 0 đến 9:"))
    if index_duong > 9 :
        print("sai")
        if index_duong < 0:
            print("với số nhỏ hơn không thì là trường hợp khác")
        else:
            print("tuple=:" , tuple[index_duong])
        index_am = int(input("nhập index từ -1 đến -9:"))
        if index_am < -9 :
            print("index ngoài phạm vi yêu cầu")
        if index_am > -1:
            print("index này của trường hợp trên:")
    else:
        print("tuple=:", tuple[index_am] )
        s_find = input("nhập chuỗi để xem nó xuất hiện bao lần: ")
        dem= tuple.count(s_find)
        print("phần tử s_find xuất hiện:", dem ,"lần") 

#12
def bai_12():
    a = input("nhập các phần tử:").split(' ')
    b = input("nhập các phần tử:").split(' ')
    tuple_a = tuple(a)
    tuple_b = tuple(b)  
    tuple_c = tuple_a + tuple_b
    print("tuple c:", tuple_c)
    tuple_d  = tuple(sorted(tuple_c))
    print("tuple_d:", tuple_d)
    print(" 3 phần tửi cuối cùng của tuple_d là:", tuple_d[-3:])