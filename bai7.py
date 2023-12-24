A=[]
while True:
    gia_tri=input("nhập giá trị:\n")
    A.append(gia_tri)
    tiep_tuc=input("thêm giá trị 1:đồng ý, 0:thôi\n")
    if tiep_tuc!='1':
        break
thresh = input("nhập thresh:")
ket_qua = [ i > thresh for i in A ]
print("kết quả: ", ket_qua)   