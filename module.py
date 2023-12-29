import csv
def doc_tap_tin_csv(ten_tap_tin):
    try:
        with open(ten_tap_tin, 'r', newline='', encoding='utf-8') as file:
            doc_csv = csv.reader(file)
            for row in doc_csv:
                print(row)
    except FileNotFoundError:
        print("Không tìm thấy tập tin. Vui lòng kiểm tra lại tên tập tin.")
    except Exception as e:
        print("Đã xảy ra lỗi:", e)