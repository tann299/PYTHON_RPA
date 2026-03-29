#1.Viết chương trình giải phương trình bậc 2
# import math

# a = float(input("NHập hệ số a: "))
# b = float(input("Nhập hệ số b: "))
# c = float(input("NHập hệ số c: "))
# if a == 0:
#     if b == 0:
#         print("Phương trình vô nghiệm")
#     else:
#         print("Phương trình có 1 nghiệm x = ",-c/b)

# else:
#     delta = b*b - 4*a*c

#     if delta > 0:
#         x1 = (-b + math.sqrt(delta))/ (2*a)
#         x2 = (-b - math.sqrt(delta))/ (2*a)
#         print("Phương trình có 2 nghiệm phân biệt:")
#         print("x1 = ",x1)
#         print("x2 = ",x2)
#     elif delta == 0:
#         x1 = -b / (2*a) 
#         print("Phương trình có nghiệm kép x1 = x2 = ",x1)
#     else:
#         print("Phương trình vô nghiệm")

#2.2. Viết chương trình in ra bảng cửu chương từ 2 đến 9
# for i in range(1,11):
#     line = ""
#     for j in range(2,10):
#         line += f"{j} x {i:2} = {i*j:2} | " 
#     print(" "+line+" ")

#3.Tính tổng các số chẵn từ 1 đến 100
# tong = 0
# for i in range(0,101):
#     if i % 2 == 0:
#         tong += i
# print("Tong cac so chan la: ",tong)

#4.Viết chương trình kiểm tra số nguyên tố
# import math

# n = int(input("Nhập số cần kiểm tra: "))

# if n < 2:
#     print(f"{n} không phải là số nguyên tố")
# else:
#     is_prime = True 

#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             is_prime = False 
#             break 
            
#     if is_prime:
#         print(f"{n} là số nguyên tố")
#     else:
#         print(f"{n} không phải là số nguyên tố")

#5. In ra hình tam giác so với chiều cao n
# n = int(input("Nhập chiều cao : "))
# for i in range(1,n+1):
#     for j in range(i):
#         print("* ", end="")
#     print()

#6. Viết chương trình tìm ƯCLN và BCNN của hai số
# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))

# so_a, so_b = a, b

# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a

# ucln = a
# bcnn = (so_a * so_b) // ucln

# print("ƯCLN là:", ucln)
# print("BCNN là:", bcnn)

#7.Viết chương trình đếm số lượng chữ số của một số nguyên
n = int(input("Nhập số nguyên: "))
dem = 0
if n==0:
    dem = 1
else:
    while n != 0:
        n //= 10
        dem += 1
print("Tổng các chữ số là : ",dem)