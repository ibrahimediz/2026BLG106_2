def kare_al(sayi):
    return sayi * sayi

sonuc = kare_al(5)
print("5'in karesi:", sonuc)

# Return edilen değeri başka bir işlemde kullanabiliriz
print("10'un karesi + 5:", kare_al(10) + 5)

def tam_ad_olustur(ad, soyad):
    return f"{ad} {soyad}"

print(tam_ad_olustur("Mehmet", "Demir"))
