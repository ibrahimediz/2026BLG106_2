# Python'da temel veri tipleri

metin = "Bu bir string ifadedir"
tam_sayi = 100
ondalikli_sayi = 3.14
dogru_yanlis = True # Boolean

print(type(metin))
print(type(tam_sayi))
print(type(ondalikli_sayi))
print(type(dogru_yanlis))

# İleri Seviye Veri Tipleri (İlerleyen haftalarda detaylı işlenecek)
liste = [1, 2, 3, "Elma"]       # Değiştirilebilir sıralı liste
demet = (10, 20, 30)            # Değiştirilemez sıralı liste (Tuple)
kume = {1, 2, 3, 3}             # Eşsiz elemanlar (Set) -> {1, 2, 3} olur
sozluk = {"isim": "Ali", "yas": 25} # Anahtar-Değer eşleşmesi (Dict)

print("-" * 20)
print("Liste Tipi:", type(liste), "->", liste)
print("Demet (Tuple) Tipi:", type(demet), "->", demet)
print("Küme (Set) Tipi:", type(kume), "->", kume)
print("Sözlük (Dict) Tipi:", type(sozluk), "->", sozluk)
print("-" * 20)

# Tip dönüşümü (Type Casting)
sayi_metni = "50"
sayi = int(sayi_metni) # String'i Integer'a çevirme
print(sayi + 10) # 60 çıktısını verir
