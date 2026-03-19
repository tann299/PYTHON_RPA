tien_goc = 1000000
lai_suat = 0.5
thoi_gian = 5 #nam

# tiền lãi sau 3 năm
tienlai_3nam = tien_goc * lai_suat * 3
print(tienlai_3nam)

# tổng tiền sau 5 năm
tong_tien = (tien_goc * lai_suat * thoi_gian) + tien_goc
print(tong_tien)
# tiền lãi trung bình
tonglai = tien_goc * lai_suat * thoi_gian
lai_tb = tonglai / thoi_gian
print(lai_tb)
