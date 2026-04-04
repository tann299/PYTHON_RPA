import pandas as pd
data = {
    'MaSV': ['SV001', 'SV002', 'SV003', 'SV004', 'SV005', 'SV006', 'SV007', 'SV008', 'SV009', 'SV010'],
    'HoTen': ['Nguyễn Văn An', 'Trần Thị Bình', 'Lê Hoàng Cường', 'Phạm Minh Đức', 'Đỗ Thị Hoa', 
              'Hoàng Văn Hùng', 'Ngô Thanh Huy', 'Vũ Thu Hương', 'Đặng Đình Khoa', 'Bùi Tuyết Mai'],
    'Lop': ['CNTT1', 'CNTT2', 'CNTT1', 'CNTT3', 'CNTT2', 'CNTT1', 'CNTT3', 'CNTT2', 'CNTT1', 'CNTT3'],
    'DiemPython': [8.5, 6.0, None, 9.0, 7.5, 5.5, None, 8.0, 10.0, 4.0],
    'DiemWeb': [7.0, None, 8.0, 9.5, 6.0, None, None, 8.5, 9.0, 5.5],
    'DiemDatabase': [9.0, 7.5, 6.5,None, 8.0, 5.0, 7.0, 8.5, 9.5, None]
}

df = pd.DataFrame(data)
print(df)
# Doc file va kiem tra gia tri null
print("Số lượng null mỗi cột là: ")
print(df.isnull().sum())

#điền giá trị null = 0
df = df.fillna(0)

# Tạo cột ddiemerTB = tb 33 môn
df["DiemTB"] = (df["DiemPython"] + df["DiemWeb"] + df["DiemDatabase"]) / 3
print(df)

#Tạo cột phân loại:
def phan_loai(diem):
    if diem >= 8: return 'Giỏi'
    elif diem >= 6.5: return 'Khá'
    elif diem >= 5: return 'Trung bình'
    else: return 'Yếu'

df['XepLoai'] = df['DiemTB'].apply(phan_loai)
print(df)

#thống kê dữ liệu theo cột lớp
print("Điểm trung bình theo lớp:")
diem_theo_lop = df.groupby('Lop')['DiemTB'].mean()
print(diem_theo_lop)

# Tạo bảng thông tin lớp với 
data_lop = {
    'Lop': ['CNTT1', 'CNTT2', 'CNTT3'],
    'GiaoVien': ['Thầy Nam', 'Cô Lan', 'Thầy Sơn'],
    'PhongHoc': ['P.101', 'P.102', 'P.201']
}
df_lop = pd.DataFrame(data_lop)

#Ghép bảng
df_ket_qua = pd.merge(df, df_lop, on='Lop', how='left')
print(df_ket_qua[['MaSV', 'HoTen', 'Lop', 'DiemTB', 'XepLoai', 'GiaoVien']])