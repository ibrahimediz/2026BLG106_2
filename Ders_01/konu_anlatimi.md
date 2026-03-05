# Ders 01: Python'a Giriş ve Temel Kavramlar

Bu ders kapsamında programlamanın temellerini, Python'un çalışma mantığını, veri tiplerini, değişken atamayı ve temel giriş/çıkış işlemlerini detaylı örneklerle öğreniyoruz.

## 1. Programlama Nedir? Neden Python?
Programlama, bilgisayara belirli bir görevi yerine getirmesi için adım adım talimatlar verme işidir. Bu talimatlar bütününe ise "program" veya "yazılım" denir. Bilgisayarlar kendi başlarına düşünemezler; onları yönlendiren insan mantığıdır.

**Python**, öğrenmesi son derece kolay, sözdizimi (syntax) İngilizceye çok yakın ve okunabilirliği yüksek, genel amaçlı bir programlama dilidir. Veri bilimi, yapay zeka, web geliştirme ve otomasyon gibi birçok alanda en çok tercih edilen dildir.

## 2. İlk Python Programımız (`print` Fonksiyonu)
Python'da ekrana bir şeyler yazdırmak, kullanıcıyla iletişim kurmanın veya programın doğru çalışıp çalışmadığını test etmenin en temel yoludur. Bunun için içine tırnak işaretleriyle metin verdiğimiz `print()` fonksiyonu kullanılır.

```python
# '#' işareti yorum satırıdır. Python bu satırı kod olarak okumaz, atlar.
# Ekrana düz bir metin yazdıralım:
print("Merhaba Dünya!")
print("Python öğreniyorum ve bu çok eğlenceli.")

# Print ile sadece metin değil, matematiksel işlemlerin sonucunu da yazdırabiliriz:
print(5 + 3) # Çıktı: 8
```

## 3. Değişkenler (Variables) ve İsimlendirme Kuralları
Değişkenler, verileri hafızada (RAM) tutmak, bu verileri isimlendirmek ve program içinde defalarca kullanabilmek için oluşturduğumuz taşıyıcılardır (kutular gibi düşünebilirsiniz).

Python'da değişken tanımlarken herhangi bir tür belirtmeye gerek yoktur (`int x = 5` yerine doğrudan `x = 5` yazılır). Python akıllıdır, verinin türünü otomatik anlar.

```python
isim = "Ahmet"  # Metin tipinde değişken
yas = 20        # Tam sayı tipinde değişken
boy = 1.75      # Ondalıklı sayı tipinde değişken

# Değişkenleri kullanarak ekrana yazdırma
print("Kullanıcının adı:", isim)
print("Yaşı:", yas)

# Bir değişkenin değeri daha sonra değiştirilebilir:
yas = 21
print("Kullanıcının yeni yaşı:", yas)
```

**Değişken İsimlendirme Kuralları:**
1. Rakamla başlayamaz (`1sayi = 5` YANLIŞ, `sayi1 = 5` DOĞRU).
2. Aralarında boşluk olamaz (`ad soyad = "Ali"` YANLIŞ, `ad_soyad = "Ali"` DOĞRU).
3. Özel karakterler (%, !, @, vb.) kullanılamaz. Sadece alt çizgi `_` serbesttir.
4. Python'a ait özel kelimeler değişken adı olamaz (örn: `print = 5`, `if = 10` yapılamaz).

## 4. Veri Tipleri (Data Types)
Değişkenlerin tuttuğu verilerin özellikleri farklıdır. Bir metin ile çarpma işlemi yapamazsınız, bu yüzden bilgisayar verinin türünü (tipini) bilmek zorundadır.

**Temel Veri Tipleri:**
- **`str` (String):** Metinsel ifadelerdir. Mutlaka tek tırnak `''` veya çift tırnak `""` içinde yazılır. Örneğin `"Merhaba"`, `"12345"` (Tırnak içindeki sayılar artık metindir!)
- **`int` (Integer):** Tam sayılardır. Tırnaksız yazılır. Örneğin `-10`, `0`, `150`.
- **`float`:** Ondalıklı sayılardır. Ondalık kısmı ayırmak için virgül değil **nokta `.`** kullanılır. Örneğin `3.14`, `0.5`.
- **`bool` (Boolean):** Sadece mantıksal iki değerden birini alır: `True` (Doğru/1) veya `False` (Yanlış/0). Karar yapılarında (Eğer böyleyse bunu yap) çok sık kullanılır.

Bir verinin tipini merak ediyorsanız `type()` fonksiyonunu kullanabilirsiniz:
```python
isim = "Ayşe"
kilo = 60.5
ogrenci_mi = True

print(type(isim))        # <class 'str'>
print(type(kilo))        # <class 'float'>
print(type(ogrenci_mi))  # <class 'bool'>
```

### Tip Dönüşümü (Type Casting)
Bazen bir sayıyı metne veya bir metni sayıya çevirmemiz gerekir. Örneğin `int()` , `float()`, `str()` çevirici modüllerdir.
```python
metin_sayi = "50"
# print(metin_sayi + 10) # HATA! Metin ile sayı (int) toplanamaz.

gercek_sayi = int(metin_sayi) # '50' metnini 50 sayısına dönüştürdük.
print(gercek_sayi + 10)       # Sonuç: 60
```

## 5. Kullanıcıdan Veri Almak (`input` Fonksiyonu)
Programlarımızın interaktif olması, kullanıcının girdiği verilere göre şekillenmesi için veri almamız şarttır. `input()` komutu, programın çalışmasını durdurup kullanıcının klavyeden bir şeyler yazıp `Enter`'a basmasını bekler.

**ÇOK ÖNEMLİ KURALLAR:** `input()` ile kullanıcıdan alınan her türlü veri (kullanıcı sayı girse dahi) sistem tarafından **String (str - metin)** olarak kabul edilir. Sayısal işlem yapılacaksa muhakkak `int()` ya da `float()` içine alınmalıdır.

```python
# Temel input kullanımı
ad = input("Lütfen adınızı giriniz: ")
print("Sisteme hoş geldin", ad)

# Sayısal bir işlem için input kullanımı:
dogum_yili = input("Doğum yılınız nedir? ")
# yas = 2024 - dogum_yili # HATA verir, 2024(int) ile dogum_yili(str) çıkarılamaz.

yas = 2024 - int(dogum_yili) # Doğru kullanım
print("Demek", yas, "yaşındasınız.")
```

---

## 💻 Bölüm Sonu Egzersizleri

1. **Değişken Değiştir-Tokuş (Swap):** 
   `a = 15` ve `b = 30` adında iki değişken oluşturun. Kodunuzun ilerleyen satırlarında öyle bir işlem (veya üçüncü bir geçici değişken) yapın ki ekran çıktısında `print(a)` 30 sonucunu, `print(b)` 15 sonucunu versin.
2. **KDV Hesaplama:**
   Kullanıcıdan `input()` ile bir ürünün fiyatını girmesini isteyin (bu değer ondalıklı olabilir, tip dönüşümüne dikkat!). Girilen fiyata %20 KDV ekleyerek "Ürünün KDV dahil fiyatı: ... TL" şeklinde ekrana yazdıran programı kodlayın.
3. **Kişisel Bilgi Kartı:**
   Kullanıcıdan adını, soyadını, yaşını ve en sevdiği rengi ayrı ayrı `input()` ile alın. Sonrasında `print` ile tüm bu bilgileri birleştirerek şuna benzer bir cümle kurdurun: *"Merhaba Ali Yılmaz! 25 yaşında olduğunu ve Mavi rengini sevdiğini biliyorum."*
