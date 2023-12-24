a = input("nhập các phần tử:").split(' ')
b = input("nhập các phần tử:").split(' ')
tuple_a = tuple(a)
tuple_b = tuple(b)  
tuple_c = tuple_a + tuple_b
print("tuple c:", tuple_c)
tuple_d  = tuple(sorted(tuple_c))
print("tuple_d:", tuple_d)
print(" 3 phần tửi cuối cùng của tuple_d là:", tuple_d[-3:])
