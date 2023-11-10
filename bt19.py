so_n=int(input("số n: "))
def dao_nguoc_va_in_so_le(n):
    danh_sach_so = list(range(1, n + 1))
    danh_sach_so.reverse()
    so_le = [x for x in danh_sach_so if x % 2 != 0]
    print("số lẻ đảo ngược:", so_le)
dao_nguoc_va_in_so_le(so_n)