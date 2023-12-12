from datetime import datetime

def xem_ngay(ngay, thang, nam):
    thu_trong_tuan = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ Nhật']
    ngay_duoc_chon = datetime(nam, thang, ngay)
    
    thu = thu_trong_tuan[ngay_duoc_chon.weekday()]
    so_ngay_trong_thang = calendar.monthrange(nam, thang)[1]
    
    return thu, so_ngay_trong_thang


