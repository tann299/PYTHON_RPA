# 1. Viết chương trình nhập vào họ tên, tuổi, điểm trung bình và in ra màn hình
name = input("Nhập họ tên: ")
age = int(input("Nhập tuổi: "))
diemtb = float(input("Nhập điểm trung bình: "))

print("Họ tên:", name)
print("Tuổi:", age)
print("Điểm trung bình:", diemtb)

#2. Tính diện tích và chu vi hình chữ nhật khi biết chiều rộng và dài
chieu_rong = 3
chieu_dai = 5
chuvi = (chieu_rong + chieu_dai) * 2
dientich = chieu_rong * chieu_dai
print("Chu vi hình chữ nhật:", chuvi)
print("Diện tích hình chữ nhật:", dientich)

#3.Viết chương trình chuyển đổi độ C sang F
do_c = float(input("Nhập giá trị độ C muốn chuyển đổi:"))
do_f = (do_c*9/5) +32
print("Giá trị độ F là:", do_f)

#4. Nhập vào 1 số nguyên kiểm tra xem chẵn hay lẻ
num = int(input("Nhập vào 1 số nguyên:"))
if num % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")

#5. tính tổng hiệu thương của 2 số thực
num1 = float(input("Nhập vào số thực thứ nhất:"))
num2 = float(input("Nhập vào số thực thứ hai:"))
tong = num1 + num2
hieu = num1 - num2
if num2 != 0:
    thuong = num1 / num2
else:
    print("Không thể chia cho 0")


