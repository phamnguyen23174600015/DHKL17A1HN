# xu_ly_tap_tin_csv.py
from module13 import ghi_csv_file,doc_csv_file

def main():
    ten_tap_tin = input("Nhập tên tập tin csv: ")
    danh_ba_dien_thoai = [
        ["Tên - Số điện thoại"],
        ["Jonny", "0989"],
        ["Lucy", "753951"],
        ["8903 123456"],
        ["Jack", "0913 753951"],
        ["Johnny Lee"],
        ["Peter Son", "8913 753852"],
        ["0989 753951"],
        ["Johnnathan", "0903 123456"]
    ]

 
    ghi_csv_file(ten_tap_tin, danh_ba_dien_thoai)

    print("Nội dung tập tin sau khi ghi:")
    doc_csv_file(ten_tap_tin)

main()
