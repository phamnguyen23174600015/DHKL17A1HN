def tim_max_min(danh_sach):
    max = max(danh_sach)
    min = min(danh_sach)
    return max, min
#2
def  abss(x):
    if x > 0:
        return(x)
    else:
        return(-x)
#3   
def gia_try(x, n):
    S =((x**2+1)*n)
    return(S)
#4
def giai_pt_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        return -b / a
#5
def kt_nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False
#6
def tinh_phi_taxi():
    loai_xe = int(input("nhập loại xe (4,7): "))
    if loai_xe != 4 and loai_xe != 7:
        print("CHỈ 4 HOẶC 7")
    else:
        quang_duong = float(input("nhập quãng đường (km): "))
        if quang_duong <= 0:
            print("NHẬP LẠI QUÃNG ĐƯỜNG")
        else:
            thoi_gian_cho = int(input("nhập thởi gian chờ theo ddown vị phút: "))
            if thoi_gian_cho < 0:
                print("SAI")
            else:
                tong_tien = 0.0
                tien_cho = 0.0
                if thoi_gian_cho > 5:
                    tien_cho = (thoi_gian_cho - 5) * 800  
                if loai_xe == 4:
                    if quang_duong >= 21:
                        tong_tien = 11000 + (20 - 0.8) * 12100 + (quang_duong - 20) * 10000 + tien_cho
                    elif quang_duong > 0.8:
                        tong_tien = 11000 + (quang_duong - 0.8) * 12100 + tien_cho
                    else:
                        tong_tien = 11000 + tien_cho
                elif loai_xe == 7:
                    if quang_duong >= 21:
                        tong_tien = 13000 + (20 - 0.8) * 14100 + (quang_duong - 20) * 12000 + tien_cho
                    elif quang_duong > 0.8:
                        tong_tien = 13000 + (quang_duong - 0.8) * 14100 + tien_cho
                    else:
                        tong_tien = 13000 + tien_cho
    return f"phải thanh toán: {tong_tien} VND"
#10
def gia_tri(x, n):
    S =((x**2+1)*n)
    return(S)
#11
def gia_try(x, n):
    A=(x**2+n+1)**n +(x**2-n+1)**n
    return(A)
#12
def ktsnt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#7
def tinh_tien_dien(so_dien):
    if so_dien < 0: 
        print("So kWh khong xac dinh")
    else:
        tong_tien = 0.0
    if so_dien >= 401:
        tong_tien = 50*1.675 + 50*1734 + 100*2014 + 100*2536 + 100*2834 + (so_dien - 400)*2927
    elif so_dien >= 301: 
        tong_tien = 50*1.675 + 50*1734 + 100*2014 + 100*2536 + (so_dien - 300)*2834
    elif so_dien >= 201: 
        tong_tien = 50*1.675 + 50*1734 + 100*2014 + (so_dien - 200)*2536
    elif so_dien >= 101: 
        tong_tien = 50*1.675 + 50*1734 + (so_dien - 100)*2014
    elif so_dien >= 51:
        tong_tien = 50*1.675 + (so_dien - 50)*1734
    else: 
        tong_tien = so_dien*1.675
    print(f"tiền điện cần thanh toán: {tong_tien}")

#8
def tinh_gia_phong(ma_phong, so_dem):
    giam_gia = 0.0
    if so_dem > 1 and so_dem < 4:
        giam_gia = 0.25
    elif so_dem >= 4:
        giam_gia = 0.3
    gia_phong = 0.0
    if ma_phong == 1:
        gia_phong = 1260000
        ten_phong = "Standard"
    elif ma_phong == 2:
        gia_phong = 1550000
        ten_phong = "Superior Garden View"
    elif ma_phong == 3:
        gia_phong = 1830000
        ten_phong = "Superior Ocean View"
    elif ma_phong == 4:
        gia_phong = 1830000
        ten_phong = "Garden View Bungalow"
    elif ma_phong == 5:
        gia_phong = 2120000
        ten_phong = "Pool View Bungalow"
    elif ma_phong == 6:
        gia_phong = 2120000
        ten_phong = "Family Room"
    elif ma_phong == 7:
        gia_phong = 2540000
        ten_phong = "Beach Front Bungalow"
    elif ma_phong == 8:
        gia_phong = 4800000
        ten_phong = "VIP Sea View"
    else:
        print("Mã phòng không hợp lệ")
        return
    tong_tien = gia_phong * so_dem * (1 - giam_gia)
    print(f"mã {ma_phong} - {ten_phong} - {so_dem} đêm - giảm {giam_gia*100}%: {tong_tien}")
#9
def dem_nguoc(n):
    while n >= 0:
        print(n)
        n -= 1
    else:
        print("hết")

#14
def tinh_tong(n):
    if n < 0:
        print("sai")
    else:
        tong = 0
    for i in range(1,n+1):
        k = int(input(f"số thứ {i}: "))
        tong = tong + k
    print(f"tổng: {tong}")

#13
def tim_gt():
    n = int(input("Nhập vào số nguyên dương n: "))
    tongA = 0
    tichC = 1
    tongB = 0
    tichD = 0
    tongE = 0
    tongF = 0
    for i in range(0, n + 1):
        if i % 2 != 0:
            tongA += i
        if i%2==0:
            tongB = tongB + i
        if i%3==0:
          tichD = tichD*i

        tichC = tichC*i

    for i in range(2, n+1):
        for j in range(2,i):
            if i%j == 0:
             break
    else:
        tongE = tongE + i
        
    flag = True
    for i in range(1, n+1):
        if flag == True:
            tongF = tongF + 1.0/i
        flag = False
    else:
        tong = tongF - 1.0/i
        flag = True
       
    print(f"A = {tongA}")
    print(f"B = {tongB}")
    print(f"D = {tichD}")
    print(f"C = {tichC}")
    print(f"E = {tongE}")
    print(f"F = {tongF}")

#15
def tinh_tong_so_nguyen():
    tong = 0
    while True:
        n = int(input("Nhập số nguyên (nhập 0 để kết thúc): "))
        print(n)
        tong += n
        if n == 0:
            break
    print(f"Tổng các số vừa nhập: {tong}")

#16
def tim_ucln(a, b):
    if a < 0 or b < 0:
        print("a, b phải lớn hơn 0")
        return
    min_value = min(a, b)
    for i in range(min_value, 0, -1):
        if a % i == 0 and b % i == 0:
            print(f"UCLN({a},{b}) = {i}")
            break

#17
def tim_bcnn(a,b):
    if a < 0 or b < 0:
     if a < 0 or b < 0:
        print("a, b phai lon hon 0")
    max = a
    if max < b:
        max = b
    while True:
        if max % a == 0 and max % b == 0:
            print(f"BCNN({a},{b}) = {max}")
            break
        max = max + 1

#18
def kt_so(x):
    if x < 0:
        print("x phải dương")
    else:
        if x == 0:
            print("không không là sôs hoàn hảo")
    tong = 0
    for i in range(1, x):
        if x%i==0:
            tong = tong + i
    if tong == x:
        print(f"{x} là số hoàn hảo")
    else:
        print(f"{x} không là số hoàn hảo")
#19
def tao_day_so_moi(day_so):
    if day_so[0] != "1":
        print("Day so phai bat dau tu so 1")
        return None
    day_so_nguoc = day_so[::-1]
    pos = 0
    count = 0
    day_so_moi = ""
    for i in day_so_nguoc:
        if i == " ":
            k = day_so_nguoc[pos - count : pos]
            k = k[::-1]
            if int(k) % 2 != 0:
                day_so_moi = day_so_moi + k + " "
            count = 0
        else:
            count = count + 1
        pos = pos + 1

    day_so_moi = day_so_moi + "1"
    return day_so_moi

#20
def tinh_e_mu_x(n, x):
    if n < 0:
        print("n khong hop le")
    else:
        tong = 0
    for i in range(1,n+1):
        giai_thua = 1
        for j in range(1,i+1):
            giai_thua = giai_thua*i
        tong = tong + (x**i)/giai_thua
    print(f"e^{x} = {tong}")
  

    







