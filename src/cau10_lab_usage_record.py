from datetime import datetime

ma_phien = input()
ma_may = input()
cong_suat = float(input())
so_phut = int(input())
don_gia = float(input())

dien_nang = (cong_suat / 1000) * (so_phut / 60)
chi_phi = dien_nang * don_gia
tren_60_phut = so_phut > 60
ghi_nhan_luc = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"{ma_phien}")
print(f"{ma_may}")
print(f"{cong_suat:.2f} W")
print(f"{so_phut} phút")
print(f"{dien_nang:.3f} kWh")
print(f"{chi_phi:.2f} VND")
print(f"{tren_60_phut}")
print(f"{ghi_nhan_luc}")