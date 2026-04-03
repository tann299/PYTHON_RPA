from abc import ABC, abstractmethod

class Taikhoan(ABC):
    def __init__(self, stk, chu_tk, so_du=0):
        self._stk = stk
        self._chu_tk = chu_tk
        self._so_du = so_du

    def nap_tien(self, so_tien):
        if so_tien > 0:
            self._so_du += so_tien
            print("Nap tien thanh cong!")
        else:
            print("So tien khong hop le!")

    @abstractmethod
    def rut_tien(self, so_tien):
        pass

    def hien_thi(self):
        print(f"STK: {self._stk} | Chu: {self._chu_tk} | So du: {self._so_du}")

class tk_tietkiem(Taikhoan):
    def rut_tien(self, so_tien):
        if 0 < so_tien <= self._so_du:
            self._so_du -= so_tien
            print(f"Rut thanh cong: {so_tien}")
        else:
            print("So du khong du!")

class tk_tindung(Taikhoan):
    def __init__(self, stk, chu_tk, so_du=0, han_muc=5000000):
        super().__init__(stk, chu_tk, so_du)
        self.han_muc = han_muc

    def rut_tien(self, so_tien):
        if 0 < so_tien <= (self._so_du + self.han_muc):
            self._so_du -= so_tien
            print(f"Rut thanh cong: {so_tien}. Du no: {self._so_du}")
        else:
            print("Vuot qua han muc!")

danh_sach_tk = {}

while True:
    print("\n1. Tao TK | 2. Rut | 3. Nap | 4. Xem | 0. Thoat")
    try:
        choice = int(input("Chon: "))
        
        if choice == 0:
            break
            
        if choice == 1:
            stk = input("STK: ")
            ten = input("Ten: ")
            loai = input("Loai (1: Tiet kiem, 2: Tin dung): ")
            if loai == "1":
                danh_sach_tk[stk] = tk_tietkiem(stk, ten)
            else:
                danh_sach_tk[stk] = tk_tindung(stk, ten)
            print("Da tao xong!")

        elif choice == 2 or choice == 3:
            stk = input("Nhap STK: ")
            if stk in danh_sach_tk:
                so_tien = int(input("So tien: "))
                if choice == 2:
                    danh_sach_tk[stk].rut_tien(so_tien)
                else:
                    danh_sach_tk[stk].nap_tien(so_tien)
            else:
                print("Khong tim thay!")

        elif choice == 4:
            for tk in danh_sach_tk.values():
                tk.hien_thi()
                
    except:
        print("Loi: Phai nhap so!")