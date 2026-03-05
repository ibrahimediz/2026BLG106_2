# Ders 05: Fonksiyonlar (Metotlar) ve Kodun Modülerliği

Bu derste, programlamanın en temel yapı taşlarından biri olan **fonksiyonları** öğreneceğiz. Belirli bir işlemi yerine getiren, ihtiyaç duyduğumuzda tekrar tekrar çağırabileceğimiz "Alt Programlara (Kod Bloklarına)" fonksiyon denir. 

## 1. Neden Fonksiyon Kullanırız? (DRY Prensibi)
Yazılım dünyasında altın bir kural vardır: **Don't Repeat Yourself (DRY) - Kendini Tekrar Etme!**
Eğer aynı 10 satırlık kodu programın 5 farklı yerinde kopyala-yapıştır yapıyorsanız, o kodda bir hata çıktığında 5 farklı yeri manuel düzeltmek zorunda kalırsınız. Bunun yerine o 10 satırı bir fonksiyon içine koyup, adını 5 kez çağırırsak hem kodumuz kısalır hem de yönetimi harika olur.

## 2. Fonksiyon Tanımlama (`def`) ve Çağırma
Python'da bir fonksiyon yaratmak için `def` (İngilizce 'define' kelimesinden gelir) anahtar kelimesi kullanılır. Fonksiyonlar içlerindeki kodları, sadece biz onları **çağırırsak** isimleriyle tetiklenerek çalıştırırlar, tek başlarına tanım kısmındayken çalışmazlar.

```python
# Fonksiyonu Tanımlama (Şablonu Oluşturma)
def kullanici_karsila():
    print("Sisteme hoş geldiniz!")
    print("Bugün sizin için neler yapabilirim?")

# Fonksiyonu Çağırma (İçindeki kodlar buraya gelince çalışır)
kullanici_karsila()

# İhtiyaç oldukça programın herhangi bir yerinde DİLEDİĞİN KADAR çağır
print("--- araya başka işlemler girdi ---")
kullanici_karsila() 
```

## 3. Parametre Alan Fonksiyonlar (Dışarıdan Veri İletme)
Kullanıcıyı selamlarken hep kuru kuru "Sisteme hoş geldiniz" yerine ismini söylemek istersek, o fonksiyonun içine bir veri fırlatmamız (göndermemiz) gerekir. Atılan bu verilere argüman, fonksiyonun bunları havada yakalayıp tuttuğu değişkenlere ise **Parametre** denir.

```python
def karsila_isimle(ad, soyad): # ad ve soyad parametrelerdir
    print(f"Merhaba {ad} {soyad}, nasılsın?")

# Fonksiyona dışarıdan argüman (değer) yolluyoruz
karsila_isimle("Ahmet", "Yılmaz")
karsila_isimle("Elif", "Demir")

# Basit bir matematik örneği
def dikdortgen_cevre_hesapla(kisa, uzun):
    cevre = 2 * (kisa + uzun)
    print("Çevre uzunluğunuz:", cevre)

dikdortgen_cevre_hesapla(5, 10) # 30 yazar
```

### Varsayılan (Default) Parametreler
Bazen fonksiyon çağrıldığında kişi bir değer göndermeyi unutabilir veya bir ayar standart kalabilir. Böyle durumlarda hata vermesini engellemek için parametreye eşittir (`=`) ile varsayılan bir değer atanır.

```python
def siparis_ver(urun, miktar=1): # Eğer miktar verilmezse sistem otomatik olarak 1 kabul eder
    print(f"{miktar} adet {urun} siparişiniz alındı.")

siparis_ver("Bilgisayar", 3) # "3 adet Bilgisayar..." (miktar=3 oldu)
siparis_ver("Mouse")         # "1 adet Mouse..." (Miktar yollamadık, varsayılanı(1) kullandı!)
```

## 4. `return` Kavramı (Değer Döndürme)
`print()` ekranda görsel bir yazı gösterir ama hesaplanan o sayı programın içinde silinir gider. Diyelim ki 5 ile 10'u bir fonksiyona toplattınız. Bu toplamın (15'in) yarısına matematikte ihtiyacınız olacak. İşte fonksiyonun işi bitince, hesapladığı sonucu ana programa **geri taşıtan (fırlatan)** sihirli kelime `return`'dür.

```python
def kdv_hesapla(fiyat):
    kdvli_fiyat = fiyat * 1.20 # Yüzde 20 kdv eklendi
    return kdvli_fiyat # Bu hesaplanan bedeli çağrıldığı yere geri ver!

sonuc = kdv_hesapla(100)
# Artık elimde "sonuc" isminde ve "120" değerinde somut bir matematiksel veri var.
# Bunu print ile de yazdırabilirim, başka sayılarla da carpabilirim.
print("Müşteriden istenecek bedel:", sonuc, "TL")

# Daha karmaşık kullanım:
aylik_taksit = sonuc / 6
print("6 Taksit seçenekli aylık ödeme:", aylik_taksit)
```

*(Not: Fonksiyon içinde `return` kelimesini gördüğü anda fonksiyon derhal BİTER ve içinden ÇIKILIR, return kelimesinden sonrasına yazılan kodlar okunmaz.)*

---

## 💻 Bölüm Sonu Egzersizleri

1. **Selamlama ve Yaş Hesaplayıcı Fonksiyonu:**
   Parametre olarak `isim` ve `dogum_yili` alan bir `kisi_analiz()` fonksiyonu tanımlayın. Bu fonksiyon içeride şimdiki yıldan (2024'ten) doğum yılını çıkararak kişinin yaşını bulsun.
   Sonra *sadece ekrana* (print ile) `"Merhaba Ali, demek 30 yaşındasın."` yazdırsın. Geriye (return) değer dönmesine **gerek yoktur**.

2. **Geometri Modülü (Return Uygulaması):**
   1. `daire_alani(yaricap)` isminde bir fonksiyon oluşturun. Dairenin alanını hesaplasın (pi = 3). **Ve sonucu return etsin**.
   2. `kure_hacmi(yaricap)` adında bir ikinci fonksiyon oluşturun. Bir kürenin hacmi = (4/3) * pi * (yaricap ** 3)'tür. Alanı hesaplarken pi=3 alın. *Zorluk:* Kürenin bu formüldeki yarıçap işlemlerinde ilk yaptığımız alan fonksiyonundan yararlanmaya kalkmayın, doğrudan formülü kullanıp bulduğunuz Hacim sonucunu `return` edin.
   3. `print()` ile `kure_hacmi(5)` diyerek sonucu konsolda görün.

3. **Asal Sayı Dedektörü (Zor):**
   Parametre olarak sadece 1 tek **"sayı"** alan bir `asal_mi(sayi)` fonksiyonu yapınız.
   - Bildiğiniz üzere asal sayılar 1'e ve kendisine bölünebilen, başka hiçbir şeye tam bölünemeyen (`sayi % x == 0`) sayılardır.
   - Fonksiyon içinde bir `for loop (range)` kullanarak sayıyı 2'den başlayıp kendisine kadar olan sayılara bölmeye çalışın. (Örn 13 için; 2,3,4,5...12'ye sırayla böldürün).
   - *Eğer içeride bölen bir sayıya rastlarsa*, fonksiyon derhal `return False` yapsın.
   - *Eğer for döngüsü hiç False'a takılmadan sağ salim biterse*, dışarıda `return True` yapsın.
   - Dışarıdan 25 ve 17 gibi 2 sayıyı ayrı ayrı yollayarak fonksiyonu test edip dönen `True` veya `False` değerlerini ekrana bastırın.
