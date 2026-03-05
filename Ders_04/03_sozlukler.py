ogrenci = {
    "no": 123,
    "ad": "Ayşe",
    "soyad": "Yılmaz",
    "dersler": ["Matematik", "Fizik"]
}

print("Öğrenci Adı:", ogrenci["ad"])
print("Öğrenci No:", ogrenci["no"])

# Yeni alan ekleme
ogrenci["sinif"] = 4
print("Güncel sözlük:", ogrenci)

# Anahtarları gezme
for key in ogrenci.keys():
    print(key)

# Değerleri gezme
for value in ogrenci.values():
    print(value)

print("-" * 20)

# get() metodu: Anahtar yoksa hata vermez, None veya belirtilen değeri döner
print("Bölüm:", ogrenci.get("bolum", "Belirtilmemiş")) # Belirtilmemiş döner

#items() metodu: Anahtar ve değeri aynı anda alma
print("\nSözlük İçeriği:")
for k, v in ogrenci.items():
    print(f"{k}: {v}")

# update() metodu: Başka bir sözlükle veya verilerle güncelleme
ogrenci.update({"yas": 26, "sehir": "İstanbul"})
print("\nGüncel:", ogrenci)

# pop() metodu: Eleman silme ve değerini alma
silinen_sinif = ogrenci.pop("sinif")
print(f"\nSilinen sınıf bilgisi: {silinen_sinif}")
print("Son hali:", ogrenci)
