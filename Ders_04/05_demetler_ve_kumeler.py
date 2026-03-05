# DEMETLER (TUPLES)
# Listelere benzerler ancak elemanları DEĞİŞTİRİLEMEZ (Immutable).
# Parantez () ile tanımlanır.

renkler = ("Kırmızı", "Yeşil", "Mavi")
print("Demet:", renkler)
print("İlk Eleman:", renkler[0])

# renkler[0] = "Sarı" # HATA! Demetler değiştirilemez.

# Tek elemanlı demet tanımlarken virgül konulmalıdır
tek_elemanli = (1,)
print("Tip:", type(tek_elemanli))

# KÜMELER (SETS)
# Eşsiz elemanlardan oluşur (Aynı eleman birden fazla olamaz).
# Sırasızdır (İndeks ile erişilemez).
# Süslü parantez {} ile tanımlanır.

sayilar = {1, 2, 3, 3, 4, 4, 5} # Tekrar edenler otomatik silinir
print("Küme:", sayilar) # {1, 2, 3, 4, 5}

# Kümeye eleman ekleme
sayilar.add(6)
print("Eklendi:", sayilar)

# Kümeden eleman çıkarma
sayilar.remove(2)
print("Silindi:", sayilar)

# Kümelerde matematiksel işlemler
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Birleşim (Union):", a | b) # {1, 2, 3, 4, 5, 6}
print("Kesişim (Intersection):", a & b) # {3, 4}
print("Fark (Difference):", a - b) # {1, 2}
