from pprint import pprint #Thêm thư viện để hiện thông tin đẹp mắt hơn
class DongVat:
    def __init__(self, id, ten, loai, can_nang, anh = None, dia_chi = None):
        self.id = id
        self.ten = ten
        self.loai = loai
        self.can_nang = can_nang
        self.anh = anh
        self.dia_chi = dia_chi
    def update(self, thong_tin_moi:dict): #Hàm cập nhật, thay thông tin mới
            #Thuộc tính nào trống thì sẽ không cập nhật
            for attribute, value in thong_tin_moi.items():
                if value:
                    setattr(self, attribute, value)
lis_dong_vat = []
def nhap_thong_tin():
    soluong = int(input("Mời bạn nhập số con vật muốn thêm: "))
    for i in range(soluong):
        print("Thông tin con vật thứ ",i+1)
        id = input("Mời bạn nhập ID: ")
        ten = input("Mời bạn nhập tên: ")
        can_nang = input("Mời bạn nhập cân nặng: ")
        loai = input("Mời nhập loài: ")     
        anh = input("Mời nhập link ảnh: ")     
        dia_chi = input("Mời nhập địa chỉ: ")
        i = DongVat(id, ten, loai, can_nang, anh, dia_chi)
        lis_dong_vat.append(i)
def hien_thong_tin():
    for i in lis_dong_vat:
        print(f" \n Con vật có mã {i.id} là: ")
        pprint(f"Tên là {i.ten} thuộc loài {i.loai}, nặng {i.can_nang}, sống tại {i.dia_chi}")   
nhap_thong_tin()
hien_thong_tin()   