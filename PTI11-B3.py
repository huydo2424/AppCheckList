def bo_phim():
    from pprint import pprint #Thêm thư viện pprint để in ra theo dạng đẹp mắt hơn
    class BoPhim:
        def __init__(self, id, tieu_de, ngay_dang, anh = None, danh_gia = None, link = None):
            self.id = id
            self.tieu_de = tieu_de
            self.ngay_dang = ngay_dang
            self.anh = anh
            self.danh_gia = danh_gia
            self.link = link
        def update(self, thong_tin_moi:dict): #Hàm cập nhật, thay thông tin mới
            #Thuộc tính nào trống thì sẽ không cập nhật
            for attribute, value in thong_tin_moi.items():
                if value:
                    setattr(self, attribute, value)
    phim1 = BoPhim(1, "Phim siêu nhân", "23-05-2025", "anh1.jpg", 4.9, "youtube.com")
    print("Phim 1 nguyên bản sẽ có thông tin sau:")
    pprint(phim1.__dict__) #Hiện thông tin dưới dạng dict
    thong_tin_moi = { #Khai báo thông tin cần cập nhật vào biến thong_tin_moi
        "tieu_de": "Phim Nobita",
        "danh_gia": 4.1
    }
    phim1.update(thong_tin_moi) #gọi hàm cập nhật thông tin vừa khai báo
    print("Phim 1 sau khi được cập nhật sẽ có thông tin là:")
    pprint(phim1.__dict__)
    phim2 = BoPhim(2, "Phim chiến đấu", "23-05-2025", "anh2.jpg", 4.9, "youtube.com")
    phim3 = BoPhim(3, "Phim tình cảm", "23-05-2025", "anh3.jpg", 4.9, "youtube.com")
    phim4 = BoPhim(4, "Phim nghiện game", "23-05-2025", "anh4.jpg", 4.9, "youtube.com")
    phim5 = BoPhim(5, "Video học tập", "23-05-2025", "anh5.jpg", 4.9, "youtube.com")
    bo_phim = [phim1, phim2, phim3, phim4, phim5] #Tổng hợp các thông tin theo dạng danh sách
    print("********  Đây là thông tin phim    *************")
    def hien_thong_tin():
        for i in bo_phim:
            print("\nBộ phim có mã phim là", i.id)
            pprint(i.__dict__)
    hien_thong_tin()
    #Chức năng xoá 1 bộ phim nào đó
    ten_phim_xoa = input("Mời bạn nhập tên muốn xoá: ")
    for phim in bo_phim:
        if phim.tieu_de == ten_phim_xoa:
            bo_phim.remove(phim)
    print("Danh sách sau khi xoá là: \n")
    hien_thong_tin()
    #Viết class dành cho tài khoản người dùng gồm: id, tên, ten_dang_nhap, mat_khau, SDT. Viết hàm cập nhật SDT hoặc tên. Viết hàm xoá theo id, nhập đúng id thì xoá người đó.