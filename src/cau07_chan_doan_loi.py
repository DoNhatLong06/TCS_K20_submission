ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kwh")
#chay lan 1:
#src/cau07_chan_doan_loi.py, dong 2, loai loi:TypeError, tb loi: khong ho tro phep toan chia giua 'str' va 'int'
#nguyen nhan: do cong_suat_w dang nhap tu input() se mang kieu chuoi(str) nen k tinh toan duoc
#cach sua: thay doi cong_suat_w = float(input("nhap cong suat W:"))
#chay lan 2:
#/src/cau07_chan_doan_loi.py, dong 6,loai loi: NameError, tbao loi: dien_nang is not defined
#nguyen nhan: dong 22 ghi la dien_nang_kwh nhung dong 24 ghi dien_nang
#cach sua: doi thanh dien_nang_kwh
#chay lan 3:
#/src/cau07_chan_doan_loi.py, dong 6, loai loi:SyntaxError, tb loi: dau '(" chua dc dong lai
#nguyen nhan: thieu dau ')'
#cach sua: them dau ')' vao cuoi dong code
