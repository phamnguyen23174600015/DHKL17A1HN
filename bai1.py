def tim_max_min(danh_sach):
    max = max(danh_sach)
    min = min(danh_sach)
    return max_value, min_value

danh_sach = int(input("nhap cac so:"))
max, min = tim_max_min(danh_sach)
print("max: ", max)  
print("min: ", min)  