ma_phien = input()
ma_may = input()
cong_suat = float(input())
so_phut = int(input())
don_gia = float(input())
dien_nang = (cong_suat / 1000) * (so_phut / 60)
chi_phi = dien_nang * don_gia
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang}")
print(f"Chi phí: {chi_phi}")


