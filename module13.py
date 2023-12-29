def bai1(ten):
    with open(ten,'r') as file:
            nd = file.read()
            print("nd: ", nd)


def bai2(ten):
      with open(ten,'r') as file:
            nd = file.read()
            so_dong = nd.count('\n')
            so_tu = len(nd.split())
            ki_tu = len(nd)
            print("nd: ", nd)
            print("sd: ", so_dong)
            print("kt: ", ki_tu)
            print("st: ", so_tu)
      

def doc(ten):
      with open(ten,'r') as file:
            nd = file.read()
            print("nd: ", nd)

def ghi(ten , noi_dung):
    with open(ten, 'w') as file:
        file.write(noi_dung)
                 
import csv
def mo_file_danh_sach():
    try:
        with open('ds_sach_sach.csv','r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Danh sách không tồn tại: ")

import csv
def ghi_csv_file(ten_tap_tin, noi_dung):
    with open(ten_tap_tin, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(noi_dung)

def doc_csv_file(ten_tap_tin):
    with open(ten_tap_tin, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
