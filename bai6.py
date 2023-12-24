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