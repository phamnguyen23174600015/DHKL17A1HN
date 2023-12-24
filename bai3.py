list_of_animals=input("nhập các con thú: ").split(' ')
print(f"số lượng các con thú là:", {len(list_of_animals)})
con_thu_can_tim=input("nhập con thú cần tìm: ")
if con_thu_can_tim in list_of_animals:
    print(f"con {con_thu_can_tim} có trong danh sách trên")
else:
    print(f"con {con_thu_can_tim} không có trong danh sách")