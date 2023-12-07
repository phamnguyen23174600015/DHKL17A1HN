import math
r, a, b = map(float, input("Nhap ban kinh va 2 canh cua hinh chu nhat: ").split(','))
if a == b:
    print("voi so nhap tren thi khong co hinh chu nhat nao o day")
else:
    pi=3.14
    s_hcn=a*b
    p_hcn=(a+b)*2
    s_ht=pi * r**2
    p_ht=2*pi*r
    print("chu vi va dien tich ht va hcn lan luot la",p_ht,s_ht,p_hcn,s_hcn)