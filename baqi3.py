import math
can_nang=float(input("can nang(kg):"))
chieu_cao=float(input("chieu cao(m):"))
bmi=can_nang/math.pow(chieu_cao,2)
if bmi>25:
    print("ban beo qua va bmi cua ban la:", bmi )
if bmi>18 and bmi<25:
    print("ban on roi va bmi cua m la:", bmi )
else:
    print("ban gay qua va bmi cua ban la:", bmi )
