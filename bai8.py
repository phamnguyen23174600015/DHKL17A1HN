A = input("nhập các số có thể là số may mắn:").split(' ')
so_may_man = [num for num in A if int(num) % 7 == 0]
print("số may mắn là:", so_may_man)