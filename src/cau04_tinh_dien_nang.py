cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000 
dien_nang_kwh = cong_suat_w * so_phut /60
chi_phi = dien_nang_kwh * don_gia_kwh 
print (dien_nang_kwh, type(dien_nang_kwh))
print (chi_phi, type(chi_phi))
#DU DOAN: lan 1: so phut = 90
#dien nang tieu thu = 0.375 kwh (kieu du lieu: <class 'float'>)
#chi phi dien = 1125.0 (kieu du lieu: <class 'float'>)
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60
chi_phi= dien_nang_kwh * don_gia_kwh
print (dien_nang_kwh, type(dien_nang_kwh))
print (chi_phi, type(chi_phi))
